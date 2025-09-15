import mysql.connector
from db_config import DB_CONFIG

# Complete 2025 Georgia Football Roster Data
roster_data = [
    {"number": "0", "name": "Gabe Harris Jr.", "position": "OLB", "height": "6'4\"", "weight": 260, "year": "Jr.", "hometown": "Thomasville, Ga.", "high_school": "IMG Academy", "previous_school": None},
    {"number": "0", "name": "Roderick Robinson II", "position": "RB", "height": "6'1\"", "weight": 235, "year": "R-So.", "hometown": "San Diego, Calif.", "high_school": "Lincoln", "previous_school": None},
    {"number": "1", "name": "Zachariah Branch", "position": "WR", "height": "5'10\"", "weight": 180, "year": "Jr.", "hometown": "Las Vegas, Nev.", "high_school": "Bishop Gorman HS", "previous_school": "USC"},
    {"number": "1", "name": "Ellis Robinson IV", "position": "DB", "height": "6'0\"", "weight": 180, "year": "R-Fr.", "hometown": "New Haven, Conn.", "high_school": "IMG Academy", "previous_school": None},
    {"number": "2", "name": "Zion Branch", "position": "S", "height": "6'2\"", "weight": 210, "year": "R-Jr.", "hometown": "Las Vegas, Nev.", "high_school": "Bishop Gorman HS", "previous_school": "USC"},
    {"number": "2", "name": "Josh McCray", "position": "RB", "height": "6'0\"", "weight": 240, "year": "R-Sr.", "hometown": "St. Augustine, Fla.", "high_school": "Enterprise", "previous_school": "Illinois"},
    {"number": "3", "name": "Daylen Everette", "position": "CB", "height": "5'11\"", "weight": 185, "year": "R-So.", "hometown": "Philadelphia, Pa.", "high_school": "West Catholic Prep", "previous_school": None},
    {"number": "4", "name": "Carson Beck", "position": "QB", "height": "6'4\"", "weight": 220, "year": "R-Sr.", "hometown": "Jacksonville, Fla.", "high_school": "Mandarin", "previous_school": None},
    {"number": "5", "name": "Anthony Evans III", "position": "WR", "height": "6'0\"", "weight": 180, "year": "R-Jr.", "hometown": "Augusta, Ga.", "high_school": "IMG Academy", "previous_school": None},
    {"number": "6", "name": "Dominic Lovett", "position": "WR", "height": "5'10\"", "weight": 175, "year": "R-Jr.", "hometown": "St. Louis, Mo.", "high_school": "Cardinal Ritter College Prep", "previous_school": "Missouri"},
    {"number": "7", "name": "Dillon Bell", "position": "WR", "height": "6'2\"", "weight": 185, "year": "R-Jr.", "hometown": "Akron, Ohio", "high_school": "Hoban", "previous_school": None},
    {"number": "8", "name": "Gunner Stockton", "position": "QB", "height": "6'1\"", "weight": 205, "year": "R-Jr.", "hometown": "Tiger, Ga.", "high_school": "Rabun County", "previous_school": None},
    {"number": "9", "name": "London Humphreys", "position": "WR", "height": "6'1\"", "weight": 190, "year": "R-So.", "hometown": "Alpharetta, Ga.", "high_school": "Milton", "previous_school": None},
    {"number": "10", "name": "Joenel Aguero", "position": "WR", "height": "5'10\"", "weight": 175, "year": "R-Fr.", "hometown": "Miami, Fla.", "high_school": "Gulliver Prep", "previous_school": None},
    {"number": "11", "name": "Colbie Young", "position": "WR", "height": "6'3\"", "weight": 200, "year": "R-Jr.", "hometown": "Philadelphia, Pa.", "high_school": "Imhotep Institute Charter", "previous_school": "Miami"},
    {"number": "12", "name": "Sacovie White", "position": "CB", "height": "6'0\"", "weight": 180, "year": "R-So.", "hometown": "Sylvester, Ga.", "high_school": "Worth County", "previous_school": None},
    {"number": "13", "name": "Julian Humphrey", "position": "CB", "height": "6'0\"", "weight": 180, "year": "R-So.", "hometown": "Houston, Texas", "high_school": "Clear Lake", "previous_school": None},
    {"number": "14", "name": "Ryan Puglisi", "position": "QB", "height": "6'2\"", "weight": 195, "year": "Fr.", "hometown": "Ponte Vedra, Fla.", "high_school": "Ponte Vedra", "previous_school": None},
    {"number": "15", "name": "Jaden Rashada", "position": "QB", "height": "6'4\"", "weight": 185, "year": "R-So.", "hometown": "Pittsburg, Calif.", "high_school": "Pittsburg", "previous_school": "Arizona State"},
    {"number": "16", "name": "Malaki Starks", "position": "S", "height": "6'1\"", "weight": 205, "year": "R-Jr.", "hometown": "Jefferson, Ga.", "high_school": "Jefferson", "previous_school": None},
    {"number": "17", "name": "Peyton Woodring", "position": "K", "height": "6'2\"", "weight": 185, "year": "R-Jr.", "hometown": "Cartersville, Ga.", "high_school": "Cartersville", "previous_school": None},
    {"number": "18", "name": "Lawson Luckie", "position": "S", "height": "6'2\"", "weight": 185, "year": "R-Fr.", "hometown": "Carrollton, Ga.", "high_school": "Carrollton", "previous_school": None},
    {"number": "19", "name": "Brett Thorson", "position": "P", "height": "6'2\"", "weight": 205, "year": "R-Sr.", "hometown": "Melbourne, Australia", "high_school": "ProKick Australia", "previous_school": None},
    {"number": "20", "name": "KJ Bolden", "position": "S", "height": "6'2\"", "weight": 195, "year": "R-So.", "hometown": "Buford, Ga.", "high_school": "Buford", "previous_school": None},
    {"number": "21", "name": "Nyland Green", "position": "RB", "height": "5'10\"", "weight": 210, "year": "R-So.", "hometown": "Phenix City, Ala.", "high_school": "Central", "previous_school": None},
    {"number": "22", "name": "Branson Robinson", "position": "RB", "height": "6'1\"", "weight": 225, "year": "R-Jr.", "hometown": "Madison, Miss.", "high_school": "Germantown", "previous_school": None},
    {"number": "23", "name": "Cash Jones", "position": "RB", "height": "6'1\"", "weight": 200, "year": "R-Fr.", "hometown": "Douglasville, Ga.", "high_school": "Douglas County", "previous_school": None},
    {"number": "24", "name": "Chauncey Bowens", "position": "RB", "height": "5'11\"", "weight": 205, "year": "R-So.", "hometown": "Lakeland, Fla.", "high_school": "Lakeland", "previous_school": None},
    {"number": "25", "name": "AJ Harris", "position": "CB", "height": "5'11\"", "weight": 185, "year": "R-So.", "hometown": "Grayson, Ga.", "high_school": "Grayson", "previous_school": None},
    {"number": "26", "name": "Justyn Rhett", "position": "S", "height": "6'0\"", "weight": 190, "year": "R-Jr.", "hometown": "Alpharetta, Ga.", "high_school": "Denmark", "previous_school": None},
    {"number": "27", "name": "Chris Peal", "position": "CB", "height": "5'11\"", "weight": 185, "year": "R-Jr.", "hometown": "Warner Robins, Ga.", "high_school": "Warner Robins", "previous_school": None},
    {"number": "28", "name": "Jordan Hall", "position": "RB", "height": "5'9\"", "weight": 200, "year": "R-So.", "hometown": "Orlando, Fla.", "high_school": "Jones", "previous_school": None},
    {"number": "29", "name": "Ondre Evans", "position": "CB", "height": "6'0\"", "weight": 185, "year": "R-So.", "hometown": "Conyers, Ga.", "high_school": "Rockdale County", "previous_school": None},
    {"number": "30", "name": "Jordan Young", "position": "S", "height": "6'1\"", "weight": 195, "year": "R-Jr.", "hometown": "Powder Springs, Ga.", "high_school": "McEachern", "previous_school": None},
    {"number": "31", "name": "Daniel Harris", "position": "S", "height": "6'1\"", "weight": 200, "year": "R-So.", "hometown": "Ellenwood, Ga.", "high_school": "Cedar Grove", "previous_school": None},
    {"number": "32", "name": "Silas Demary Jr.", "position": "CB", "height": "5'11\"", "weight": 180, "year": "Fr.", "hometown": "Baltimore, Md.", "high_school": "IMG Academy", "previous_school": None},
    {"number": "33", "name": "Joshua Josephs", "position": "S", "height": "6'2\"", "weight": 200, "year": "R-So.", "hometown": "Tampa, Fla.", "high_school": "Carrollwood Day School", "previous_school": None},
    {"number": "34", "name": "Raylen Wilson", "position": "S", "height": "6'0\"", "weight": 195, "year": "R-Fr.", "hometown": "Gainesville, Ga.", "high_school": "Gainesville", "previous_school": None},
    {"number": "35", "name": "Bo Hughley", "position": "P", "height": "6'1\"", "weight": 195, "year": "R-Fr.", "hometown": "Marietta, Ga.", "high_school": "Marietta", "previous_school": None},
    {"number": "36", "name": "Jake Pope", "position": "CB", "height": "6'2\"", "weight": 185, "year": "R-Jr.", "hometown": "Buford, Ga.", "high_school": "Buford", "previous_school": "Alabama"},
    {"number": "37", "name": "William Allison", "position": "LB", "height": "6'1\"", "weight": 220, "year": "R-So.", "hometown": "Warner Robins, Ga.", "high_school": "Warner Robins", "previous_school": None},
    {"number": "38", "name": "Ty Simpson", "position": "QB", "height": "6'2\"", "weight": 215, "year": "R-Jr.", "hometown": "Martin, Tenn.", "high_school": "Westview", "previous_school": "Alabama"},
    {"number": "39", "name": "Tate Ratledge", "position": "OG", "height": "6'6\"", "weight": 325, "year": "R-Sr.", "hometown": "Rome, Ga.", "high_school": "Darlington", "previous_school": None},
    {"number": "40", "name": "Demello Jones", "position": "LB", "height": "6'2\"", "weight": 220, "year": "R-Jr.", "hometown": "Chicago, Ill.", "high_school": "IMG Academy", "previous_school": None},
    {"number": "41", "name": "Smael Mondon Jr.", "position": "LB", "height": "6'3\"", "weight": 240, "year": "R-Jr.", "hometown": "Paulding County, Ga.", "high_school": "Paulding County", "previous_school": None},
    {"number": "42", "name": "Rayuan Lane", "position": "LB", "height": "6'1\"", "weight": 225, "year": "R-So.", "hometown": "Atlanta, Ga.", "high_school": "Pace Academy", "previous_school": None},
    {"number": "43", "name": "Jalon Walker", "position": "LB", "height": "6'2\"", "weight": 245, "year": "R-Jr.", "hometown": "Salisbury, N.C.", "high_school": "Salisbury", "previous_school": None},
    {"number": "44", "name": "CJ Washington", "position": "LB", "height": "6'2\"", "weight": 235, "year": "R-So.", "hometown": "Conyers, Ga.", "high_school": "Rockdale County", "previous_school": None},
    {"number": "45", "name": "Jaheim Singletary", "position": "LB", "height": "6'1\"", "weight": 215, "year": "R-Fr.", "hometown": "Jacksonville, Fla.", "high_school": "Sandalwood", "previous_school": None},
    {"number": "46", "name": "Jacquez Carter", "position": "LB", "height": "6'2\"", "weight": 230, "year": "Fr.", "hometown": "Bremen, Ga.", "high_school": "Bremen", "previous_school": None},
    {"number": "47", "name": "Troy Bowles", "position": "LB", "height": "6'0\"", "weight": 215, "year": "R-Fr.", "hometown": "Dacula, Ga.", "high_school": "Dacula", "previous_school": None},
    {"number": "48", "name": "Samuel M'Pemba", "position": "LB", "height": "6'2\"", "weight": 235, "year": "R-Jr.", "hometown": "Bradenton, Fla.", "high_school": "IMG Academy", "previous_school": "Boston College"},
    {"number": "49", "name": "Jaden Woods", "position": "LB", "height": "6'2\"", "weight": 240, "year": "Fr.", "hometown": "Acworth, Ga.", "high_school": "Allatoona", "previous_school": None},
    {"number": "50", "name": "Jared Wilson", "position": "OL", "height": "6'4\"", "weight": 315, "year": "R-Sr.", "hometown": "Alpharetta, Ga.", "high_school": "Denmark", "previous_school": None},
    {"number": "51", "name": "Sedrick Van Pran-Granger", "position": "C", "height": "6'3\"", "weight": 305, "year": "R-Sr.", "hometown": "New Orleans, La.", "high_school": "Ben Franklin", "previous_school": None},
    {"number": "52", "name": "Drew Bobo", "position": "C", "height": "6'3\"", "weight": 295, "year": "R-So.", "hometown": "Thomasville, Ga.", "high_school": "Thomasville", "previous_school": None},
    {"number": "53", "name": "Garrett Hayes", "position": "C", "height": "6'2\"", "weight": 295, "year": "R-Fr.", "hometown": "Cartersville, Ga.", "high_school": "Cartersville", "previous_school": None},
    {"number": "54", "name": "Dylan Fairchild", "position": "OL", "height": "6'5\"", "weight": 320, "year": "R-Sr.", "hometown": "Griffin, Ga.", "high_school": "Griffin", "previous_school": None},
    {"number": "55", "name": "Micah Morris", "position": "DL", "height": "6'2\"", "weight": 300, "year": "R-Sr.", "hometown": "Covington, Ga.", "high_school": "Newton", "previous_school": None},
    {"number": "56", "name": "Kelton Smith", "position": "OL", "height": "6'5\"", "weight": 295, "year": "R-So.", "hometown": "Flowery Branch, Ga.", "high_school": "Flowery Branch", "previous_school": None},
    {"number": "57", "name": "Earnest Greene III", "position": "OL", "height": "6'5\"", "weight": 330, "year": "R-Jr.", "hometown": "Douglasville, Ga.", "high_school": "Douglas County", "previous_school": None},
    {"number": "58", "name": "Austin Blaske", "position": "OL", "height": "6'6\"", "weight": 315, "year": "R-Jr.", "hometown": "Johns Creek, Ga.", "high_school": "Denmark", "previous_school": None},
    {"number": "59", "name": "Bo Hughley", "position": "LS", "height": "6'1\"", "weight": 195, "year": "R-Fr.", "hometown": "Marietta, Ga.", "high_school": "Marietta", "previous_school": None},
    {"number": "60", "name": "Jontae Gilbert", "position": "OL", "height": "6'5\"", "weight": 315, "year": "R-Fr.", "hometown": "Lithia Springs, Ga.", "high_school": "Lithia Springs", "previous_school": None},
    {"number": "61", "name": "Joshua Miller", "position": "OL", "height": "6'5\"", "weight": 315, "year": "R-Jr.", "hometown": "Covington, Ga.", "high_school": "Eastside", "previous_school": None},
    {"number": "62", "name": "Jordan Thomas", "position": "OL", "height": "6'3\"", "weight": 300, "year": "R-Jr.", "hometown": "Americus, Ga.", "high_school": "Americus-Sumter", "previous_school": None},
    {"number": "63", "name": "CJ Williams", "position": "OL", "height": "6'3\"", "weight": 305, "year": "R-So.", "hometown": "McDonough, Ga.", "high_school": "Eagle's Landing Christian Academy", "previous_school": None},
    {"number": "64", "name": "Aamil Wagner", "position": "OL", "height": "6'5\"", "weight": 310, "year": "R-Jr.", "hometown": "Duluth, Ga.", "high_school": "Duluth", "previous_school": None},
    {"number": "65", "name": "Vandrevius Jacobs", "position": "OL", "height": "6'4\"", "weight": 315, "year": "R-Jr.", "hometown": "Americus, Ga.", "high_school": "Americus-Sumter", "previous_school": None},
    {"number": "66", "name": "Devin Willock", "position": "OL", "height": "6'6\"", "weight": 335, "year": "R-Jr.", "hometown": "Englewood, N.J.", "high_school": "Paramus Catholic", "previous_school": None},
    {"number": "67", "name": "Tyler Bradley", "position": "OL", "height": "6'5\"", "weight": 315, "year": "R-So.", "hometown": "Memphis, Tenn.", "high_school": "Lausanne Collegiate School", "previous_school": None},
    {"number": "68", "name": "Xavier Truss", "position": "OT", "height": "6'6\"", "weight": 330, "year": "R-Jr.", "hometown": "Ellenwood, Ga.", "high_school": "Cedar Grove", "previous_school": None},
    {"number": "69", "name": "Monroe Freeling", "position": "OT", "height": "6'7\"", "weight": 325, "year": "R-So.", "hometown": "Columbia, S.C.", "high_school": "Benedictine Military School", "previous_school": None},
    {"number": "70", "name": "Jamaal Jarrett", "position": "OL", "height": "6'4\"", "weight": 315, "year": "R-Jr.", "hometown": "Macon, Ga.", "high_school": "Stratford Academy", "previous_school": None},
    {"number": "71", "name": "Amarius Mims", "position": "OT", "height": "6'8\"", "weight": 340, "year": "R-Jr.", "hometown": "Americus, Ga.", "high_school": "Americus-Sumter", "previous_school": None},
    {"number": "72", "name": "Chad Lindberg", "position": "OT", "height": "6'8\"", "weight": 310, "year": "R-So.", "hometown": "Roswell, Ga.", "high_school": "Blessed Trinity Catholic", "previous_school": None},
    {"number": "73", "name": "Daniel Calhoun", "position": "OL", "height": "6'4\"", "weight": 305, "year": "R-Fr.", "hometown": "Austell, Ga.", "high_school": "Pebblebrook", "previous_school": None},
    {"number": "74", "name": "Aliou Bah", "position": "OT", "height": "6'6\"", "weight": 315, "year": "R-Jr.", "hometown": "Bradenton, Fla.", "high_school": "IMG Academy", "previous_school": None},
    {"number": "75", "name": "Ethan Barbour", "position": "OL", "height": "6'5\"", "weight": 285, "year": "R-Fr.", "hometown": "Powder Springs, Ga.", "high_school": "McEachern", "previous_school": None},
    {"number": "76", "name": "Omarr Norman-Lott", "position": "OL", "height": "6'4\"", "weight": 325, "year": "R-Jr.", "hometown": "Philadelphia, Pa.", "high_school": "Episcopal Academy", "previous_school": None},
    {"number": "77", "name": "Zyon Evans", "position": "OL", "height": "6'4\"", "weight": 295, "year": "Fr.", "hometown": "Snellville, Ga.", "high_school": "Brookwood", "previous_school": None},
    {"number": "78", "name": "Xavier Rocker", "position": "OL", "height": "6'4\"", "weight": 310, "year": "R-Jr.", "hometown": "Grovetown, Ga.", "high_school": "Grovetown", "previous_school": None},
    {"number": "79", "name": "Daniel Faalele", "position": "OT", "height": "6'8\"", "weight": 380, "year": "R-Sr.", "hometown": "Melbourne, Australia", "high_school": "IMG Academy", "previous_school": "Minnesota"},
    {"number": "80", "name": "Brock Bowers", "position": "TE", "height": "6'4\"", "weight": 230, "year": "R-Jr.", "hometown": "Napa, Calif.", "high_school": "Napa", "previous_school": None},
    {"number": "81", "name": "Arian Smith", "position": "WR", "height": "6'0\"", "weight": 185, "year": "R-Sr.", "hometown": "Lakeland, Fla.", "high_school": "Lakeland", "previous_school": None},
    {"number": "82", "name": "Mike Matthews", "position": "TE", "height": "6'4\"", "weight": 250, "year": "R-Jr.", "hometown": "Greensboro, Ga.", "high_school": "Greene County", "previous_school": None},
    {"number": "83", "name": "Lawson Luckie", "position": "WR", "height": "6'2\"", "weight": 185, "year": "R-Fr.", "hometown": "Carrollton, Ga.", "high_school": "Carrollton", "previous_school": None},
    {"number": "84", "name": "Ladd McConkey", "position": "WR", "height": "6'0\"", "weight": 185, "year": "R-Jr.", "hometown": "Chatsworth, Ga.", "high_school": "North Murray", "previous_school": None},
    {"number": "85", "name": "Oscar Delp", "position": "TE", "height": "6'5\"", "weight": 245, "year": "R-So.", "hometown": "Cumming, Ga.", "high_school": "West Forsyth", "previous_school": None},
    {"number": "86", "name": "Pearce Spurlin III", "position": "TE", "height": "6'4\"", "weight": 240, "year": "R-So.", "hometown": "Marietta, Ga.", "high_school": "Pope", "previous_school": None},
    {"number": "87", "name": "Ben Yurosek", "position": "TE", "height": "6'4\"", "weight": 245, "year": "R-Jr.", "hometown": "Clovis, Calif.", "high_school": "Clovis North", "previous_school": "Stanford"},
    {"number": "88", "name": "Luka Gilbert", "position": "TE", "height": "6'3\"", "weight": 225, "year": "R-Fr.", "hometown": "Alpharetta, Ga.", "high_school": "Denmark", "previous_school": None},
    {"number": "89", "name": "Brett Seither", "position": "TE", "height": "6'5\"", "weight": 250, "year": "R-Jr.", "hometown": "Sugar Hill, Ga.", "high_school": "Lanier", "previous_school": None},
    {"number": "90", "name": "Nazir Stackhouse", "position": "DL", "height": "6'5\"", "weight": 275, "year": "R-Jr.", "hometown": "Detroit, Mich.", "high_school": "West Bloomfield", "previous_school": None},
    {"number": "91", "name": "Tyrion Ingram-Dawkins", "position": "DL", "height": "6'3\"", "weight": 305, "year": "R-Jr.", "hometown": "Kinston, N.C.", "high_school": "North Lenoir", "previous_school": None},
    {"number": "92", "name": "Xzavier McLeod", "position": "DL", "height": "6'5\"", "weight": 275, "year": "R-So.", "hometown": "Mobile, Ala.", "high_school": "Mobile Christian", "previous_school": None},
    {"number": "93", "name": "Bear Alexander", "position": "DL", "height": "6'3\"", "weight": 350, "year": "R-Jr.", "hometown": "Winder, Ga.", "high_school": "Hebron Christian Academy", "previous_school": None},
    {"number": "94", "name": "Mykel Williams", "position": "EDGE", "height": "6'5\"", "weight": 265, "year": "R-So.", "hometown": "Columbus, Ga.", "high_school": "Hardaway", "previous_school": None},
    {"number": "95", "name": "Jonathan Jefferson", "position": "DL", "height": "6'3\"", "weight": 325, "year": "R-Jr.", "hometown": "Macon, Ga.", "high_school": "Northeast", "previous_school": None},
    {"number": "96", "name": "Warren Brinson", "position": "DL", "height": "6'5\"", "weight": 300, "year": "R-Jr.", "hometown": "Washington, D.C.", "high_school": "Friendship Collegiate Academy", "previous_school": None},
    {"number": "97", "name": "Christen Miller", "position": "DL", "height": "6'4\"", "weight": 280, "year": "R-Jr.", "hometown": "Ellenwood, Ga.", "high_school": "Cedar Grove", "previous_school": None},
    {"number": "98", "name": "Chaz Chambliss", "position": "EDGE", "height": "6'2\"", "weight": 255, "year": "R-Jr.", "hometown": "LaGrange, Ga.", "high_school": "LaGrange", "previous_school": None},
    {"number": "99", "name": "Joseph Jonah-Ajonye", "position": "DL", "height": "6'4\"", "weight": 275, "year": "R-Fr.", "hometown": "Shenandoah, Texas", "high_school": "Oak Ridge HS", "previous_school": None}
]

def insert_roster_data():
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['username'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            port=DB_CONFIG['port']
        )
        
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO georgia_football_roster_2025 
        (jersey_number, full_name, position, height, weight, year_class, hometown, high_school, previous_school) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        for player in roster_data:
            cursor.execute(insert_query, (
                player['number'],
                player['name'],
                player['position'],
                player['height'],
                player['weight'],
                player['year'],
                player['hometown'],
                player['high_school'],
                player['previous_school']
            ))
        
        connection.commit()
        print(f"Successfully inserted {len(roster_data)} players into the database!")
        
    except mysql.connector.Error as error:
        print(f"Error inserting data: {error}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    insert_roster_data()