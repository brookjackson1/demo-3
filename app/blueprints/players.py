from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db
import pandas as pd

players = Blueprint('players', __name__)

@players.route('/')
def show_players():
    connection = get_db()
    
    # Check if we need to load data for modals
    edit_player = None
    delete_player = None
    result = []
    
    edit_id = request.args.get('edit_id')
    delete_id = request.args.get('delete_id')
    
    # Check database connection once
    if connection is None:
        flash("Database connection failed. Please check your database configuration.", "error")
    else:
        try:
            if edit_id:
                query = "SELECT * FROM georgia_football_roster_2025 WHERE id = %s"
                with connection.cursor() as cursor:
                    cursor.execute(query, (edit_id,))
                    edit_player = cursor.fetchone()
            
            if delete_id:
                query = "SELECT * FROM georgia_football_roster_2025 WHERE id = %s"
                with connection.cursor() as cursor:
                    cursor.execute(query, (delete_id,))
                    delete_player = cursor.fetchone()
            
            # Get all players for the table
            query = "SELECT * FROM georgia_football_roster_2025 ORDER BY CAST(jersey_number AS UNSIGNED), full_name"
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                
        except Exception as e:
            flash(f"Database error: {e}", "error")
            result = []
    
    if result:
        df = pd.DataFrame(result)
        # Add edit and delete buttons to the Actions column
        def create_actions(row):
            id = row['id']
            return (f'<a href="{url_for("players.show_players", edit_id=id)}" class="btn btn-sm btn-info">Edit</a> '
                   f'<a href="{url_for("players.show_players", delete_id=id)}" class="btn btn-sm btn-danger">Delete</a>')
        
        df['Actions'] = df.apply(create_actions, axis=1)
        table_html = df.to_html(classes='table table-striped table-bordered', index=False, header=False, escape=False)
        rows_only = table_html.split('<tbody>')[1].split('</tbody>')[0]
    else:
        rows_only = ""
    
    return render_template("players.html", table=rows_only, edit_player=edit_player, delete_player=delete_player)

@players.route('/edit/<int:player_id>', methods=['POST'])
def edit_player(player_id):
    connection = get_db()
    
    jersey_number = request.form.get('jersey_number')
    full_name = request.form.get('full_name')
    position = request.form.get('position')
    height = request.form.get('height')
    weight = request.form.get('weight', type=int, default=0)
    year_class = request.form.get('year_class')
    hometown = request.form.get('hometown')
    high_school = request.form.get('high_school')
    previous_school = request.form.get('previous_school')
    
    query = """
    UPDATE georgia_football_roster_2025
    SET jersey_number = %s, full_name = %s, position = %s, height = %s, weight = %s, 
        year_class = %s, hometown = %s, high_school = %s, previous_school = %s
    WHERE id = %s
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (jersey_number, full_name, position, height, weight, 
                              year_class, hometown, high_school, previous_school, player_id))
    connection.commit()
    
    flash("Player updated successfully!", "success")
    return redirect(url_for('players.show_players'))

@players.route('/delete/<int:player_id>', methods=['POST'])
def delete_player(player_id):
    connection = get_db()
    query = "DELETE FROM georgia_football_roster_2025 WHERE id = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, (player_id,))
    connection.commit()
    
    flash("Player deleted successfully!", "success")
    return redirect(url_for('players.show_players'))

@players.route('/add', methods=['GET', 'POST'])
def add_player():
    if request.method == 'GET':
        return render_template("add_player.html")
    
    # POST method - original add player logic
    connection = get_db()
    
    jersey_number = request.form.get('jersey_number')
    full_name = request.form.get('full_name')
    position = request.form.get('position')
    height = request.form.get('height')
    weight = request.form.get('weight', type=int, default=0)
    year_class = request.form.get('year_class')
    hometown = request.form.get('hometown')
    high_school = request.form.get('high_school')
    previous_school = request.form.get('previous_school')
    
    query = """
    INSERT INTO georgia_football_roster_2025 (jersey_number, full_name, position, height, weight, 
                                            year_class, hometown, high_school, previous_school)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (jersey_number, full_name, position, height, weight, 
                              year_class, hometown, high_school, previous_school))
    connection.commit()
    
    flash("New player added successfully!", "success")
    return redirect(url_for('players.show_players'))