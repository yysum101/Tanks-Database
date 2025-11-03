from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    template = """ 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Home</title>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
            <style>
                :root {
                    --primary: #1a1f2e;
                    --secondary: #2a3147;
                    --accent: #ff7b00;
                    --accent-light: #ff9a3d;
                    --text: #f4f4f4;
                    --text-light: #b0b8d1;
                    --success: #00d26a;
                    --danger: #ff4757;
                    --warning: #ffa502;
                    --info: #2ed573;
                    --gradient: linear-gradient(135deg, #1a1f2e 0%, #2a3147 100%);
                    --card-gradient: linear-gradient(145deg, #23283d, #1c2132);
                    --header-gradient: linear-gradient(90deg, #ff7b00 0%, #ff9a3d 100%);
                }

                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    font-family: 'Poppins', sans-serif;
                    background: var(--gradient);
                    color: var(--text);
                    min-height: 100vh;
                    padding-top: 80px;
                }

                .header {
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    width: 100%;
                    z-index: 1030;
                    background: var(--header-gradient);
                    color: #fff;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    padding: 0.8rem 2rem;
                    min-height: 70px;
                    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
                }

                .header h2 {
                    font-weight: 700;
                    font-size: 1.8rem;
                    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
                }

                .header-button {
                    background-color: transparent;
                    color: #fff;
                    border: 2px solid #fff;
                    padding: 10px 20px;
                    border-radius: 8px;
                    text-decoration: none;
                    font-size: 15px;
                    font-weight: 500;
                    transition: all 0.3s ease;
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                }

                .header-button:hover,
                .header-button:focus {
                    background-color: rgba(255, 255, 255, 0.15);
                    color: #fff;
                    transform: translateY(-2px);
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                }

                .container {
                    width: 100%;
                    max-width: 1400px;
                    margin: 0 auto;
                    padding: 0 20px;
                }

                .page-title {
                    text-align: center;
                    margin: 2rem 0;
                    font-size: 2.5rem;
                    font-weight: 700;
                    background: linear-gradient(90deg, #ff7b00, #ff9a3d);
                    -webkit-background-clip: text;
                    background-clip: text;
                    -webkit-text-fill-color: transparent;
                    text-shadow: 0 2px 10px rgba(255, 123, 0, 0.3);
                }

                .filters-container {
                    display: flex;
                    gap: 20px;
                    padding: 20px;
                    flex-wrap: wrap;
                    align-items: center;
                    justify-content: center;
                    background: rgba(42, 49, 71, 0.7);
                    border-radius: 16px;
                    margin: 20px auto;
                    max-width: 1200px;
                    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
                    backdrop-filter: blur(10px);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                }

                .filters-container input, .filters-container select {
                    padding: 12px 18px;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    border-radius: 10px;
                    font-size: 15px;
                    background: rgba(26, 31, 46, 0.8);
                    color: var(--text);
                    min-width: 180px;
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                }

                .filters-container input:focus, .filters-container select:focus {
                    outline: none;
                    border-color: var(--accent);
                    box-shadow: 0 0 0 3px rgba(255, 123, 0, 0.3);
                }

                .filters-container input::placeholder {
                    color: var(--text-light);
                }

                .filters-container select option {
                    background: var(--secondary);
                    color: var(--text);
                }

                .grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
                    gap: 25px;
                    padding: 20px;
                    justify-items: center;
                }

                .card {
                    background: var(--card-gradient);
                    border-radius: 16px;
                    padding: 20px;
                    text-align: center;
                    transition: all 0.4s ease;
                    width: 100%;
                    max-width: 300px;
                    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
                    position: relative;
                    overflow: hidden;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                }

                .card::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    height: 4px;
                    background: var(--accent);
                }

                .card:hover {
                    transform: translateY(-10px);
                    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
                }

                .card h3 {
                    font-size: 1.4rem;
                    margin-bottom: 10px;
                    color: #fff;
                    font-weight: 600;
                }

                .tier {
                    color: var(--accent);
                    font-size: 14px;
                    font-weight: 500;
                    margin: 10px 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 8px;
                }

                .branch {
                    font-size: 13px;
                    color: var(--text-light);
                    margin-top: 8px;
                    line-height: 1.4;
                }

                .card-icon {
                    font-size: 2.5rem;
                    margin-bottom: 15px;
                    color: var(--accent);
                }

                .country-flag {
                    font-size: 1.2rem;
                    margin-right: 8px;
                }

                .stats {
                    display: flex;
                    justify-content: space-between;
                    margin-top: 15px;
                    padding-top: 15px;
                    border-top: 1px solid rgba(255, 255, 255, 0.1);
                }

                .stat {
                    text-align: center;
                    flex: 1;
                }

                .stat-value {
                    font-weight: 600;
                    font-size: 1.1rem;
                    color: var(--accent);
                }

                .stat-label {
                    font-size: 0.75rem;
                    color: var(--text-light);
                }

                .card-footer {
                    margin-top: 15px;
                    padding-top: 15px;
                    border-top: 1px solid rgba(255, 255, 255, 0.1);
                    font-size: 0.85rem;
                    color: var(--text-light);
                }

                .progress-bar {
                    height: 6px;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 3px;
                    margin-top: 5px;
                    overflow: hidden;
                }

                .progress-fill {
                    height: 100%;
                    background: var(--accent);
                    border-radius: 3px;
                }

                /* Responsive adjustments */
                @media (max-width: 1200px) {
                    .grid {
                        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                    }
                }

                @media (max-width: 768px) {
                    .filters-container {
                        flex-direction: column;
                        align-items: stretch;
                    }
                    
                    .filters-container input, .filters-container select {
                        min-width: 100%;
                    }
                    
                    .grid {
                        grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
                    }
                    
                    .header {
                        padding: 0.8rem 1rem;
                    }
                    
                    .header h2 {
                        font-size: 1.5rem;
                    }
                }

                @media (max-width: 480px) {
                    .grid {
                        grid-template-columns: 1fr;
                    }
                    
                    .page-title {
                        font-size: 2rem;
                    }
                }

                /* Animation for cards */
                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(20px); }
                    to { opacity: 1; transform: translateY(0); }
                }

                .card {
                    animation: fadeIn 0.5s ease forwards;
                }

                /* Scrollbar styling */
                ::-webkit-scrollbar {
                    width: 10px;
                }

                ::-webkit-scrollbar-track {
                    background: var(--primary);
                }

                ::-webkit-scrollbar-thumb {
                    background: var(--accent);
                    border-radius: 5px;
                }

                ::-webkit-scrollbar-thumb:hover {
                    background: var(--accent-light);
                }
            </style>
        </head>
        <body>
            <nav class="navbar navbar-dark py-3" style="background: linear-gradient(90deg, #4facfe, #00f2fe);">
            <div class="container">
                <div class="header">
                        <h2 class="font">Tank Database Home</h2>
                    <div>
                        <a href="{{ url_for('tanks') }}" class="header-button" style="margin-right: 20px;"><i class="fas fa-search"></i> Tanks</a>
                    </div>
                </div>
            </div>
        </nav>
        <div style="text-align: center; margin-top: 40px;">
            <h1 style="font-family: 'Poppins', sans-serif;">Welcome to the Tank Database</h1>
            <hr style="width: 50%; margin: 20px auto; border: 1px solid #ccc;">
            <p style="font-family: 'Poppins', sans-serif; font-size: 18px; line-height: 1.4; max-width: 800px; margin: 0 auto;">
                Welcome to the ultimate Tank Database, your one-stop destination for exploring a wide variety of tanks from different eras and classifications. 
                Whether you're a history enthusiast, a military aficionado, or just curious about armored vehicles, this database has something for everyone.
            </p>
            <p style="font-family: 'Poppins', sans-serif; font-size: 18px; line-height: 1.4; max-width: 800px; margin: 20px auto;">
                Use the navigation bar above to access the comprehensive guide, where you'll find detailed information about tank mechanics, classifications, and their roles in history. 
                Dive into the tank database to explore individual tanks, their tiers, classes, and upgrade paths. 
                Discover the fascinating world of armored vehicles and their evolution over time.
            </p>
            <p style="font-family: 'Poppins', sans-serif; font-size: 18px; line-height: 1.4; max-width: 800px; margin: 20px auto;">
                Start your journey now and uncover the stories behind these incredible machines. 
                From light reconnaissance tanks to heavy-duty behemoths, the Tank Database is here to fuel your curiosity and expand your knowledge.
            </p>
            <p style="font-family: 'Poppins', sans-serif; font-size: 18px; line-height: 1.4; max-width: 800px; margin: 20px auto;">
                Don't forget to check out our featured tanks section, where we highlight some of the most iconic and historically significant tanks. 
                Learn about their design, development, and the roles they played in shaping military history.
            </p>
            <p style="font-family: 'Poppins', sans-serif; font-size: 18px; line-height: 1.4; max-width: 800px; margin: 20px auto;">
                Stay tuned for updates as we continuously expand our database with new entries, detailed guides, and fascinating insights into the world of armored vehicles. 
                Your journey into the realm of tanks begins here—explore, learn, and enjoy!
            </p>
        </div>
        </body>
        </html>
    """
    return render_template_string(template)

@app.route('/tanks')
def tanks():
    tanks = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Tank Database</title>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
            <style>
                :root {
                    --primary: #1a1f2e;
                    --secondary: #2a3147;
                    --accent: #ff7b00;
                    --accent-light: #ff9a3d;
                    --text: #f4f4f4;
                    --text-light: #b0b8d1;
                    --success: #00d26a;
                    --danger: #ff4757;
                    --warning: #ffa502;
                    --info: #2ed573;
                    --gradient: linear-gradient(135deg, #1a1f2e 0%, #2a3147 100%);
                    --card-gradient: linear-gradient(145deg, #23283d, #1c2132);
                    --header-gradient: linear-gradient(90deg, #ff7b00 0%, #ff9a3d 100%);
                }

                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    font-family: 'Poppins', sans-serif;
                    background: var(--gradient);
                    color: var(--text);
                    min-height: 100vh;
                    padding-top: 80px;
                }

                .header {
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    width: 100%;
                    z-index: 1030;
                    background: var(--header-gradient);
                    color: #fff;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    padding: 0.8rem 2rem;
                    min-height: 70px;
                    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
                }

                .header h2 {
                    font-weight: 700;
                    font-size: 1.8rem;
                    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
                }

                .header-button {
                    background-color: transparent;
                    color: #fff;
                    border: 2px solid #fff;
                    padding: 10px 20px;
                    border-radius: 8px;
                    text-decoration: none;
                    font-size: 15px;
                    font-weight: 500;
                    transition: all 0.3s ease;
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                }

                .header-button:hover,
                .header-button:focus {
                    background-color: rgba(255, 255, 255, 0.15);
                    color: #fff;
                    transform: translateY(-2px);
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                }

                .container {
                    width: 100%;
                    max-width: 1400px;
                    margin: 0 auto;
                    padding: 0 20px;
                }

                .page-title {
                    text-align: center;
                    margin: 2rem 0;
                    font-size: 2.5rem;
                    font-weight: 700;
                    background: linear-gradient(90deg, #ff7b00, #ff9a3d);
                    -webkit-background-clip: text;
                    background-clip: text;
                    -webkit-text-fill-color: transparent;
                    text-shadow: 0 2px 10px rgba(255, 123, 0, 0.3);
                }

                .filters-container {
                    display: flex;
                    gap: 20px;
                    padding: 20px;
                    flex-wrap: wrap;
                    align-items: center;
                    justify-content: center;
                    background: rgba(42, 49, 71, 0.7);
                    border-radius: 16px;
                    margin: 20px auto;
                    max-width: 1200px;
                    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
                    backdrop-filter: blur(10px);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                }

                .filters-container input, .filters-container select {
                    padding: 12px 18px;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    border-radius: 10px;
                    font-size: 15px;
                    background: rgba(26, 31, 46, 0.8);
                    color: var(--text);
                    min-width: 180px;
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                }

                .filters-container input:focus, .filters-container select:focus {
                    outline: none;
                    border-color: var(--accent);
                    box-shadow: 0 0 0 3px rgba(255, 123, 0, 0.3);
                }

                .filters-container input::placeholder {
                    color: var(--text-light);
                }

                .filters-container select option {
                    background: var(--secondary);
                    color: var(--text);
                }

                .grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
                    gap: 25px;
                    padding: 20px;
                    justify-items: center;
                }

                .card {
                    background: var(--card-gradient);
                    border-radius: 16px;
                    padding: 20px;
                    text-align: center;
                    transition: all 0.4s ease;
                    width: 100%;
                    max-width: 300px;
                    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
                    position: relative;
                    overflow: hidden;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                }

                .card::before {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    height: 4px;
                    background: var(--accent);
                }

                .card:hover {
                    transform: translateY(-10px);
                    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
                }

                .card h3 {
                    font-size: 1.4rem;
                    margin-bottom: 10px;
                    color: #fff;
                    font-weight: 600;
                }

                .tier {
                    color: var(--accent);
                    font-size: 14px;
                    font-weight: 500;
                    margin: 10px 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 8px;
                }

                .branch {
                    font-size: 13px;
                    color: var(--text-light);
                    margin-top: 8px;
                    line-height: 1.4;
                }

                .card-icon {
                    font-size: 2.5rem;
                    margin-bottom: 15px;
                    color: var(--accent);
                }

                .country-flag {
                    font-size: 1.2rem;
                    margin-right: 8px;
                }

                .stats {
                    display: flex;
                    justify-content: space-between;
                    margin-top: 15px;
                    padding-top: 15px;
                    border-top: 1px solid rgba(255, 255, 255, 0.1);
                }

                .stat {
                    text-align: center;
                    flex: 1;
                }

                .stat-value {
                    font-weight: 600;
                    font-size: 1.1rem;
                    color: var(--accent);
                }

                .stat-label {
                    font-size: 0.75rem;
                    color: var(--text-light);
                }

                .card-footer {
                    margin-top: 15px;
                    padding-top: 15px;
                    border-top: 1px solid rgba(255, 255, 255, 0.1);
                    font-size: 0.85rem;
                    color: var(--text-light);
                }

                .progress-bar {
                    height: 6px;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 3px;
                    margin-top: 5px;
                    overflow: hidden;
                }

                .progress-fill {
                    height: 100%;
                    background: var(--accent);
                    border-radius: 3px;
                }

                /* Responsive adjustments */
                @media (max-width: 1200px) {
                    .grid {
                        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                    }
                }

                @media (max-width: 768px) {
                    .filters-container {
                        flex-direction: column;
                        align-items: stretch;
                    }
                    
                    .filters-container input, .filters-container select {
                        min-width: 100%;
                    }
                    
                    .grid {
                        grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
                    }
                    
                    .header {
                        padding: 0.8rem 1rem;
                    }
                    
                    .header h2 {
                        font-size: 1.5rem;
                    }
                }

                @media (max-width: 480px) {
                    .grid {
                        grid-template-columns: 1fr;
                    }
                    
                    .page-title {
                        font-size: 2rem;
                    }
                }

                /* Animation for cards */
                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(20px); }
                    to { opacity: 1; transform: translateY(0); }
                }

                .card {
                    animation: fadeIn 0.5s ease forwards;
                }

                /* Scrollbar styling */
                ::-webkit-scrollbar {
                    width: 10px;
                }

                ::-webkit-scrollbar-track {
                    background: var(--primary);
                }

                ::-webkit-scrollbar-thumb {
                    background: var(--accent);
                    border-radius: 5px;
                }

                ::-webkit-scrollbar-thumb:hover {
                    background: var(--accent-light);
                }
            </style>
        </head>
        <body>
            <div class="header">
                <h2><i class="fas fa-tank"></i> Tank Database</h2>
                <div>
                    <a href="{{ url_for('home') }}" class="header-button"><i class="fas fa-home"></i> Home</a>
                </div>
            </div>

            <div class="container">
                <h1 class="page-title">World of Tanks Database</h1>
                
                <div class="filters-container">
                    <input type="text" id="search" placeholder="Search tanks..." oninput="renderTanks()">
                    <select id="countryFilter" onchange="renderTanks()">
                    <option value="">All Countries</option>
                    <option value="Germany">Germany</option>
                    <option value="Soviet Union">Soviet Union</option>
                    <option value="USA">United States</option>
                    <option value="UK">United Kingdom</option>
                    <option value="France">France</option>
                    <option value="Japan">Japan</option>
                    <option value="China">China</option>
                    </select>
                    <select id="classFilter" onchange="renderTanks()">
                    <option value="">All Classes</option>
                    <option value="Light">Light</option>
                    <option value="Medium">Medium</option>
                    <option value="Heavy">Heavy</option>
                    <option value="Tank Destroyer">Tank Destroyer</option>
                    </select>
                    <select id="tierFilter" onchange="renderTanks()">
                    <option value="">All Tiers</option>
                    <option value="1">Tier I</option>
                    <option value="2">Tier II</option>
                    <option value="3">Tier III</option>
                    <option value="4">Tier IV</option>
                    <option value="5">Tier V</option>
                    <option value="6">Tier VI</option>
                    <option value="7">Tier VII</option>
                    <option value="8">Tier VIII</option>
                    <option value="9">Tier IX</option>
                    <option value="10">Tier X</option>
                    </select>
                    <button class="header-button" onclick="resetFilters()">Reset Filters</button>
                </div>

                <script>
                    function resetFilters() {
                    document.getElementById("search").value = "";
                    document.getElementById("countryFilter").value = "";
                    document.getElementById("classFilter").value = "";
                    document.getElementById("tierFilter").value = "";
                    renderTanks();
                    }
                </script>

                <div class="grid" id="tankGrid"></div>
            </div>

            <script>
                const tanks = [
                    // German tanks
                    {name:"Pz. II", tier:1, class:"Light", country:"Germany", next:["Pz. 35(t)"], firepower: 25, armor: 10, speed: 45},
                    {name:"Pz. 35(t)", tier:2, class:"Light", country:"Germany", next:["Pz. III"], firepower: 35, armor: 25, speed: 40},
                    {name:"Pz. III", tier:3, class:"Medium", country:"Germany", next:["Pz. IV D", "Hetzer"], firepower: 50, armor: 30, speed: 35},
                    {name:"Hetzer", tier:4, class:"Tank Destroyer", country:"Germany", next:["StuG III G"], firepower: 75, armor: 20, speed: 30},
                    {name:"StuG III G", tier:5, class:"Tank Destroyer", country:"Germany", next:["Nashorn", "Jagdpanzer IV"], firepower: 85, armor: 25, speed: 25},
                    {name:"Nashorn", tier:6, class:"Tank Destroyer", country:"Germany", next:["Sturer Emil"], firepower: 95, armor: 15, speed: 35},
                    {name:"Jagdpanzer IV", tier:6, class:"Tank Destroyer", country:"Germany", next:["Jagdpanther"], firepower: 90, armor: 40, speed: 30},
                    {name:"Sturer Emil", tier:7, class:"Tank Destroyer", country:"Germany", next:["Rhm B. WT"], firepower: 100, armor: 25, speed: 20},
                    {name:"Jagdpanther", tier:7, class:"Tank Destroyer", country:"Germany", next:["Jagdpanther II", "Ferdinand"], firepower: 95, armor: 45, speed: 35},
                    {name:"Jagdpanther II", tier:8, class:"Tank Destroyer", country:"Germany", next:["Jagdtiger"], firepower: 105, armor: 50, speed: 30},
                    {name:"Ferdinand", tier:8, class:"Tank Destroyer", country:"Germany", next:["Jagdtiger"], firepower: 110, armor: 75, speed: 20},
                    {name:"Jagdtiger", tier:9, class:"Tank Destroyer", country:"Germany", next:["Jagdpanzer E 100"], firepower: 120, armor: 80, speed: 25},
                    {name:"Jagdpanzer E 100", tier:10, class:"Tank Destroyer", country:"Germany", next:[], firepower: 140, armor: 90, speed: 20},
                    {name:"Rhm. B. WT", tier:8, class:"Tank Destroyer", country:"Germany", next:["WT Auf Pz. IV"], firepower: 105, armor: 15, speed: 35},
                    {name:"WT Auf Pz. IV", tier:9, class:"Tank Destroyer", country:"Germany", next:["Grille 15"], firepower: 115, armor: 20, speed: 30},
                    {name:"Grille 15", tier:10, class:"Tank Destroyer", country:"Germany", next:[], firepower: 135, armor: 25, speed: 35},
                    {name:"Pz. IV D", tier:4, class:"Medium", country:"Germany", next:["VK 16.02 Leopard", "Pz. IV G"], firepower: 60, armor: 30, speed: 35},
                    {name:"Pz. IV G", tier:5, class:"Medium", country:"Germany", next:["VK 36.01H", "VK 30.01P"], firepower: 70, armor: 35, speed: 35},
                    {name:"VK 16.02 Leopard", tier:5, class:"Light", country:"Germany", next:["VK 28.01", "VK 30.01D"], firepower: 45, armor: 20, speed: 55},
                    {name:"VK 30.01D", tier:6, class:"Medium", country:"Germany", next:["Panther"], firepower: 75, armor: 40, speed: 40},
                    {name:"Panther", tier:7, class:"Medium", country:"Germany", next:["Panther II"], firepower: 85, armor: 45, speed: 40},
                    {name:"Panther II", tier:8, class:"Medium", country:"Germany", next:["E 50"], firepower: 95, armor: 50, speed: 40},
                    {name:"E 50", tier:9, class:"Medium", country:"Germany", next:["E 50 Ausf. M"], firepower: 105, armor: 60, speed: 45},
                    {name:"E 50 Ausf. M", tier:10, class:"Medium", country:"Germany", next:[], firepower: 115, armor: 70, speed: 45},
                    {name:"VK 36.01H", tier:6, class:"Heavy", country:"Germany", next:["Tiger I"], firepower: 80, armor: 60, speed: 30},
                    {name:"Tiger I", tier:7, class:"Heavy", country:"Germany", next:["Tiger II"], firepower: 90, armor: 65, speed: 30},
                    {name:"Tiger II", tier:8, class:"Heavy", country:"Germany", next:["E 75"], firepower: 100, armor: 75, speed: 25},
                    {name:"E 75", tier:9, class:"Heavy", country:"Germany", next:["E 100"], firepower: 110, armor: 85, speed: 25},
                    {name:"E 100", tier:10, class:"Heavy", country:"Germany", next:[], firepower: 130, armor: 100, speed: 20},
                    {name:"VK 30.01P", tier:6, class:"Medium", country:"Germany", next:["Tiger(P)"], firepower: 75, armor: 45, speed: 35},
                    {name:"VK 28.01", tier:6, class:"Light", country:"Germany", next:["SP I C"], firepower: 50, armor: 25, speed: 50},
                    {name:"SP I C", tier:7, class:"Light", country:"Germany", next:["RU 251"], firepower: 60, armor: 20, speed: 55},
                    {name:"RU 251", tier:8, class:"Light", country:"Germany", next:["Leopard Pt A"], firepower: 70, armor: 15, speed: 60},
                    {name:"Leopard Pt A", tier:9, class:"Medium", country:"Germany", next:["Leopard 1"], firepower: 100, armor: 30, speed: 55},
                    {name:"Leopard 1", tier:10, class:"Medium", country:"Germany", next:[], firepower: 120, armor: 35, speed: 60},
                    {name:"Tiger(P)", tier:7, class:"Heavy", country:"Germany", next:["VK 100.01P", "VK 45.02A", "Ferdinand"], firepower: 90, armor: 70, speed: 25},
                    {name:"VK 100.01P", tier:8, class:"Heavy", country:"Germany", next:["Mauschen"], firepower: 95, armor: 85, speed: 20},
                    {name:"Mauschen", tier:9, class:"Heavy", country:"Germany", next:["Maus"], firepower: 105, armor: 95, speed: 15},
                    {name:"Maus", tier:10, class:"Heavy", country:"Germany", next:[], firepower: 125, armor: 120, speed: 15},
                    {name:"VK 45.02A", tier:8, class:"Heavy", country:"Germany", next:["VK 45.02B"], firepower: 100, armor: 80, speed: 25},
                    {name:"VK 45.02B", tier:9, class:"Heavy", country:"Germany", next:["VK 72.01K"], firepower: 110, armor: 90, speed: 20},
                    {name:"VK 72.01K", tier:10, class:"Heavy", country:"Germany", next:[], firepower: 130, armor: 110, speed: 20},
                    
                    // Soviet tanks
                    {name:"T-26", tier:1, class:"Light", country:"Soviet Union", next:["BT-2"], firepower: 20, armor: 15, speed: 30},
                    {name:"BT-2", tier:2, class:"Light", country:"Soviet Union", next:["BT-7"], firepower: 30, armor: 20, speed: 50},
                    {name:"BT-7", tier:3, class:"Light", country:"Soviet Union", next:["A-20", "SU-85B"], firepower: 40, armor: 25, speed: 55},
                    {name:"A-20", tier:4, class:"Light", country:"Soviet Union", next:["T-34", "KV-1"], firepower: 45, armor: 30, speed: 60},
                    {name:"T-34", tier:5, class:"Medium", country:"Soviet Union", next:["T-34-85", "MT-25"], firepower: 65, armor: 45, speed: 50},
                    {name:"T-34-85", tier:6, class:"Medium", country:"Soviet Union", next:["T-43"], firepower: 75, armor: 50, speed: 45},
                    {name:"KV-1", tier:5, class:"Heavy", country:"Soviet Union", next:["KV-2", "KV-1S"], firepower: 70, armor: 75, speed: 25},
                    {name:"KV-2", tier:6, class:"Heavy", country:"Soviet Union", next:["KV-3"], firepower: 85, armor: 70, speed: 20},
                    {name:"KV-3", tier:7, class:"Heavy", country:"Soviet Union", next:["KV-4"], firepower: 90, armor: 80, speed: 20},
                    {name:"KV-4", tier:8, class:"Heavy", country:"Soviet Union", next:["ST-1"], firepower: 100, armor: 90, speed: 20},
                    {name:"ST-1", tier:9, class:"Heavy", country:"Soviet Union", next:["IS-4"], firepower: 110, armor: 100, speed: 25},
                    {name:"IS-4", tier:10, class:"Heavy", country:"Soviet Union", next:[], firepower: 125, armor: 120, speed: 25},
                    {name:"KV-1S", tier:6, class:"Heavy", country:"Soviet Union", next:["IS"], firepower: 80, armor: 65, speed: 35},
                    {name:"IS", tier:7, class:"Heavy", country:"Soviet Union", next:["IS-3"], firepower: 95, armor: 75, speed: 30},
                    {name:"IS-3", tier:8, class:"Heavy", country:"Soviet Union", next:["IS-8"], firepower: 105, armor: 85, speed: 30},
                    {name:"IS-8", tier:9, class:"Heavy", country:"Soviet Union", next:["IS-7"], firepower: 115, armor: 90, speed: 35},
                    {name:"IS-7", tier:10, class:"Heavy", country:"Soviet Union", next:[], firepower: 130, armor: 110, speed: 40},
                    {name:"SU-85B", tier:4, class:"Tank Destroyer", country:"Soviet Union", next:["SU-85"], firepower: 70, armor: 20, speed: 40},
                    {name:"SU-85", tier:5, class:"Tank Destroyer", country:"Soviet Union", next:["SU-100"], firepower: 80, armor: 25, speed: 35},
                    {name:"SU-100", tier:6, class:"Tank Destroyer", country:"Soviet Union", next:["SU-152","SU-100M1"], firepower: 90, armor: 30, speed: 35},
                    {name:"SU-152", tier:7, class:"Tank Destroyer", country:"Soviet Union", next:["ISU-152"], firepower: 100, armor: 35, speed: 30},
                    {name:"ISU-152", tier:8, class:"Tank Destroyer", country:"Soviet Union", next:["ISU-152"], firepower: 112, armor: 24, speed: 23},
                    {name:"Object 704", tier:9, class:"Tank Destroyer", country:"Soviet Union", next:["Object 268"], firepower: 140, armor: 30, speed:28},
                    {name:"Object 268", tier:10, class:"Tank Destroyer", country:"Soviet Union", next:[""], firepower: 174, armor: 45, speed: 41},
                    {name:"SU-100M1", tier:7, class:"Tank Destroyer", country:"Soviet Union", next:["SU-101"], firepower: 134 , armor: 34, speed:24 },
                    {name:"SU-101", tier:8, class:"Tank Destroyer", country:"Soviet Union", next:["SU-122-54"], firepower: 145 , armor: 34, speed: 34},
                    {name:"SU-122-54", tier:9, class:"Tank Destroyer", country:"Soviet Union", next:["Object 263"], firepower: 153, armor: 56, speed: 34},
                    {name:"Object 263", tier:10, class:"Tank Destroyer", country:"Soviet Union", next:[""], firepower: 170, armor: 70, speed: 10},
                ];

                function getClassIcon(tankClass) {
                    switch(tankClass) {
                        case "Light": return "fa-bolt";
                        case "Medium": return "fa-shield-alt";
                        case "Heavy": return "fa-weight-hanging";
                        case "Tank Destroyer": return "fa-crosshairs";
                        default: return "fa-tank";
                    }
                }

                function getCountryFlag(country) {
                    switch(country) {
                        case "Germany": return "🇩🇪";
                        case "Soviet Union": return "🇷🇺";
                        case "USA": return "🇺🇸";
                        case "UK": return "🇬🇧";
                        case "France": return "🇫🇷";
                        case "Japan": return "🇯🇵";
                        case "China": return "🇨🇳";
                        default: return "🏴";
                    }
                }

                function getProgressWidth(value, max = 140) {
                    return Math.min((value / max) * 100, 100);
                }

                function renderTanks() {
                    const grid = document.getElementById("tankGrid");
                    const search = document.getElementById("search").value.toLowerCase();
                    const countryFilter = document.getElementById("countryFilter").value;
                    const classFilter = document.getElementById("classFilter").value;
                    const tierFilter = document.getElementById("tierFilter").value;

                    grid.innerHTML = '';

                    const filteredTanks = tanks.filter(tank => {
                        return (
                            (countryFilter === '' || tank.country === countryFilter) &&
                            (classFilter === '' || tank.class === classFilter) &&
                            (tierFilter === '' || tank.tier.toString() === tierFilter) &&
                            (search === '' || tank.name.toLowerCase().includes(search))
                        );
                    });

                    if (filteredTanks.length === 0) {
                        grid.innerHTML = `
                            <div class="no-results" style="grid-column: 1 / -1; text-align: center; padding: 40px; color: var(--text-light);">
                                <i class="fas fa-search" style="font-size: 3rem; margin-bottom: 20px;"></i>
                                <h3>No tanks found</h3>
                                <p>Try adjusting your filters to see more results</p>
                            </div>
                        `;
                        return;
                    }

                    filteredTanks.forEach(tank => {
                        const card = document.createElement("div");
                        card.className = "card";
                        card.innerHTML = `
                            <div class="card-icon">
                                <i class="fas ${getClassIcon(tank.class)}"></i>
                            </div>
                            <h3>${tank.name}</h3>
                            <p class="tier">
                                <i class="fas fa-layer-group"></i>
                                Tier ${tank.tier} | ${tank.class}
                            </p>
                            <p class="branch">
                                <span class="country-flag">${getCountryFlag(tank.country)}</span> ${tank.country}
                            </p>
                            <div class="stats">
                                <div class="stat">
                                    <div class="stat-value">${tank.firepower}</div>
                                    <div class="stat-label">Firepower</div>
                                    <div class="progress-bar">
                                        <div class="progress-fill" style="width: ${getProgressWidth(tank.firepower)}%"></div>
                                    </div>
                                </div>
                                <div class="stat">
                                    <div class="stat-value">${tank.armor}</div>
                                    <div class="stat-label">Armor</div>
                                    <div class="progress-bar">
                                        <div class="progress-fill" style="width: ${getProgressWidth(tank.armor)}%"></div>
                                    </div>
                                </div>
                                <div class="stat">
                                    <div class="stat-value">${tank.speed}</div>
                                    <div class="stat-label">Speed</div>
                                    <div class="progress-bar">
                                        <div class="progress-fill" style="width: ${getProgressWidth(tank.speed, 60)}%"></div>
                                    </div>
                                </div>
                            </div>
                            ${tank.next.length > 0 ? 
                                `<div class="card-footer">Leads to: ${tank.next.join(', ')}</div>` : 
                                `<div class="card-footer">End of Tech Tree</div>`
                            }
                        `;
                        grid.appendChild(card);
                    });
                }

                // Initialize the page
                document.addEventListener('DOMContentLoaded', renderTanks);
            </script>
        </body>
        </html>
    """
    return render_template_string(tanks)

if __name__ == '__main__':

    app.run()
