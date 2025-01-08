from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy data for NGOs with more details
ngos = [
    {
        "name": "Helping Hands Foundation",
        "category": "Food",
        "location": "Delhi",
        "description": "Working to eliminate hunger through food distribution programs and community kitchens.",
        "contact": "+91-9876543210",
        "email": "contact@helpinghands.org",
        "address": "123, NGO Complex, Nehru Place, Delhi",
        "established": "2010",
        "beneficiaries": "10,000+ people served monthly",
        "website": "www.helpinghands.org"
    },
    {
        "name": "Cloth Care Initiative",
        "category": "Clothes",
        "location": "Noida",
        "description": "Providing clothing and dignity to underprivileged communities through donation drives.",
        "contact": "+91-9876543211",
        "email": "info@clothcare.org",
        "address": "45-A, Sector 18, Noida",
        "established": "2015",
        "beneficiaries": "5,000+ families supported",
        "website": "www.clothcare.org"
    },
    {
        "name": "EduBridge Learning",
        "category": "Education",
        "location": "Ghaziabad",
        "description": "Bridging the education gap through free tutoring and digital literacy programs.",
        "contact": "+91-9876543212",
        "email": "contact@edubridge.org",
        "address": "Plot 12, Raj Nagar, Ghaziabad",
        "established": "2012",
        "beneficiaries": "15,000+ students educated",
        "website": "www.edubridge.org"
    },
    {
        "name": "Food For All Network",
        "category": "Food",
        "location": "Noida",
        "description": "Connecting surplus food from restaurants to those in need, reducing food waste.",
        "contact": "+91-9876543213",
        "email": "support@foodforall.org",
        "address": "78-B, Sector 62, Noida",
        "established": "2018",
        "beneficiaries": "8,000+ meals served daily",
        "website": "www.foodforall.org"
    },
    {
        "name": "Dress Up India",
        "category": "Clothes",
        "location": "Delhi",
        "description": "Collecting and distributing clothes to homeless and disaster-affected communities.",
        "contact": "+91-9876543214",
        "email": "help@dressupindia.org",
        "address": "34, Civil Lines, Delhi",
        "established": "2016",
        "beneficiaries": "20,000+ garments distributed",
        "website": "www.dressupindia.org"
    },
    {
        "name": "Knowledge Path Foundation",
        "category": "Education",
        "location": "Delhi",
        "description": "Providing quality education and skill development to underprivileged youth.",
        "contact": "+91-9876543215",
        "email": "info@knowledgepath.org",
        "address": "56, Karol Bagh, Delhi",
        "established": "2014",
        "beneficiaries": "12,000+ students trained",
        "website": "www.knowledgepath.org"
    },
    {
        "name": "Roti Bank Delhi",
        "category": "Food",
        "location": "Delhi",
        "description": "Collecting excess food from events and distributing it to the needy across Delhi.",
        "contact": "+91-9876543220",
        "email": "info@rotibankdelhi.org",
        "address": "45, Lajpat Nagar, Delhi",
        "established": "2015",
        "beneficiaries": "5,000+ meals daily",
        "website": "www.rotibankdelhi.org"
    },
    {
        "name": "Hunger Heroes",
        "category": "Food",
        "location": "Noida",
        "description": "Providing nutritious meals to underprivileged children in schools.",
        "contact": "+91-9876543221",
        "email": "contact@hungerheroes.org",
        "address": "Sector 18, Noida",
        "established": "2017",
        "beneficiaries": "3,000+ children daily",
        "website": "www.hungerheroes.org"
    },
    {
        "name": "Food Warriors",
        "category": "Food",
        "location": "Ghaziabad",
        "description": "Fighting hunger through community food banks and meal programs.",
        "contact": "+91-9876543222",
        "email": "help@foodwarriors.org",
        "address": "Vaishali, Ghaziabad",
        "established": "2016",
        "beneficiaries": "7,000+ families monthly",
        "website": "www.foodwarriors.org"
    },
    {
        "name": "Annapurna Foundation",
        "category": "Food",
        "location": "Delhi",
        "description": "Providing meals to homeless and daily wage workers.",
        "contact": "+91-9876543223",
        "email": "info@annapurna.org",
        "address": "Chandni Chowk, Delhi",
        "established": "2013",
        "beneficiaries": "4,000+ meals daily",
        "website": "www.annapurna.org"
    },
    {
        "name": "Meals of Hope",
        "category": "Food",
        "location": "Noida",
        "description": "Operating mobile food vans and community kitchens.",
        "contact": "+91-9876543224",
        "email": "contact@mealsofhope.org",
        "address": "Sector 62, Noida",
        "established": "2019",
        "beneficiaries": "2,500+ people daily",
        "website": "www.mealsofhope.org"
    },
    {
        "name": "Vastra Daan",
        "category": "Clothes",
        "location": "Delhi",
        "description": "Collecting and distributing clothes to underprivileged communities.",
        "contact": "+91-9876543225",
        "email": "help@vastradaan.org",
        "address": "Pitampura, Delhi",
        "established": "2014",
        "beneficiaries": "15,000+ families annually",
        "website": "www.vastradaan.org"
    },
    {
        "name": "Clothing for All",
        "category": "Clothes",
        "location": "Ghaziabad",
        "description": "Providing new and gently used clothing to those in need.",
        "contact": "+91-9876543226",
        "email": "info@clothingforall.org",
        "address": "Indirapuram, Ghaziabad",
        "established": "2017",
        "beneficiaries": "8,000+ people served",
        "website": "www.clothingforall.org"
    },
    {
        "name": "Winter Warmth Initiative",
        "category": "Clothes",
        "location": "Delhi",
        "description": "Specialized in providing winter clothing to homeless people.",
        "contact": "+91-9876543227",
        "email": "contact@winterwarmth.org",
        "address": "Kashmere Gate, Delhi",
        "established": "2015",
        "beneficiaries": "10,000+ winter kits distributed",
        "website": "www.winterwarmth.org"
    },
    {
        "name": "Garment Bank",
        "category": "Clothes",
        "location": "Noida",
        "description": "Collecting corporate clothing donations for job seekers.",
        "contact": "+91-9876543228",
        "email": "info@garmentbank.org",
        "address": "Sector 32, Noida",
        "established": "2018",
        "beneficiaries": "5,000+ job seekers supported",
        "website": "www.garmentbank.org"
    },
    {
        "name": "Cloth of Kindness",
        "category": "Clothes",
        "location": "Ghaziabad",
        "description": "Providing clothing support to rural communities.",
        "contact": "+91-9876543229",
        "email": "help@clothofkindness.org",
        "address": "Raj Nagar Extension, Ghaziabad",
        "established": "2016",
        "beneficiaries": "12,000+ rural residents",
        "website": "www.clothofkindness.org"
    },
    {
        "name": "Shiksha Foundation",
        "category": "Education",
        "location": "Delhi",
        "description": "Providing quality education to underprivileged children.",
        "contact": "+91-9876543230",
        "email": "contact@shiksha.org",
        "address": "Dwarka, Delhi",
        "established": "2012",
        "beneficiaries": "20,000+ students educated",
        "website": "www.shiksha.org"
    },
    {
        "name": "Digital Literacy Mission",
        "category": "Education",
        "location": "Noida",
        "description": "Teaching computer skills to underprivileged youth.",
        "contact": "+91-9876543231",
        "email": "info@digitalliteracy.org",
        "address": "Sector 15, Noida",
        "established": "2016",
        "beneficiaries": "8,000+ students trained",
        "website": "www.digitalliteracy.org"
    },
    {
        "name": "Teach for Tomorrow",
        "category": "Education",
        "location": "Ghaziabad",
        "description": "Providing after-school tutoring and mentorship.",
        "contact": "+91-9876543232",
        "email": "contact@teachfortomorrow.org",
        "address": "Kavi Nagar, Ghaziabad",
        "established": "2015",
        "beneficiaries": "15,000+ students mentored",
        "website": "www.teachfortomorrow.org"
    },
    {
        "name": "Girls Education Initiative",
        "category": "Education",
        "location": "Delhi",
        "description": "Focused on promoting education for girls in underprivileged areas.",
        "contact": "+91-9876543233",
        "email": "info@girlseducation.org",
        "address": "Rohini, Delhi",
        "established": "2014",
        "beneficiaries": "10,000+ girls educated",
        "website": "www.girlseducation.org"
    },
    {
        "name": "STEM Learning Foundation",
        "category": "Education",
        "location": "Noida",
        "description": "Promoting science and technology education in schools.",
        "contact": "+91-9876543234",
        "email": "contact@stemlearning.org",
        "address": "Sector 75, Noida",
        "established": "2017",
        "beneficiaries": "6,000+ students reached",
        "website": "www.stemlearning.org"
    },
    {
        "name": "Rural Education Project",
        "category": "Education",
        "location": "Ghaziabad",
        "description": "Bringing quality education to rural areas.",
        "contact": "+91-9876543235",
        "email": "info@ruraledu.org",
        "address": "Modinagar, Ghaziabad",
        "established": "2013",
        "beneficiaries": "12,000+ rural students",
        "website": "www.ruraledu.org"
    },
    {
        "name": "Book Bank Initiative",
        "category": "Education",
        "location": "Delhi",
        "description": "Providing free textbooks and study materials to needy students.",
        "contact": "+91-9876543236",
        "email": "help@bookbank.org",
        "address": "Mayur Vihar, Delhi",
        "established": "2016",
        "beneficiaries": "25,000+ books distributed",
        "website": "www.bookbank.org"
    },
    {
        "name": "Skill Development Hub",
        "category": "Education",
        "location": "Noida",
        "description": "Vocational training for underprivileged youth.",
        "contact": "+91-9876543237",
        "email": "contact@skillhub.org",
        "address": "Sector 51, Noida",
        "established": "2015",
        "beneficiaries": "9,000+ youth trained",
        "website": "www.skillhub.org"
    },
    {
        "name": "Special Education Trust",
        "category": "Education",
        "location": "Delhi",
        "description": "Supporting education for children with special needs.",
        "contact": "+91-9876543238",
        "email": "info@specialedu.org",
        "address": "Patparganj, Delhi",
        "established": "2011",
        "beneficiaries": "3,000+ special needs children",
        "website": "www.specialedu.org"
    },
    {
        "name": "Adult Education Society",
        "category": "Education",
        "location": "Ghaziabad",
        "description": "Providing adult education and literacy programs.",
        "contact": "+91-9876543239",
        "email": "contact@adultedu.org",
        "address": "Crossing Republic, Ghaziabad",
        "established": "2014",
        "beneficiaries": "7,000+ adults educated",
        "website": "www.adultedu.org"
    },
    {
        "name": "Sahyog Care Foundation",
        "category": "Food",
        "description": "Providing meals and nutrition support to elderly and disabled.",
        "contact": "+91-9876543240",
        "email": "info@sahyogcare.org",
        "address": "Sector 128, Noida",
        "established": "2015",
        "beneficiaries": "3,000+ elderly served monthly",
        "website": "www.sahyogcare.org"
    },
    {
        "name": "Green Food Bank",
        "category": "Food",
        "description": "Sustainable food distribution and waste reduction programs.",
        "contact": "+91-9876543241",
        "email": "contact@greenfoodbank.org",
        "address": "Vasundhara, Ghaziabad",
        "established": "2018",
        "beneficiaries": "6,000+ families supported",
        "website": "www.greenfoodbank.org"
    },
    {
        "name": "Nutrition For All",
        "category": "Food",
        "description": "Focus on child nutrition and school meal programs.",
        "contact": "+91-9876543242",
        "email": "help@nutritionforall.org",
        "address": "Saket, Delhi",
        "established": "2016",
        "beneficiaries": "8,000+ children served daily",
        "website": "www.nutritionforall.org"
    },
    {
        "name": "Community Kitchen Project",
        "category": "Food",
        "description": "Running community kitchens in low-income areas.",
        "contact": "+91-9876543243",
        "email": "info@ckproject.org",
        "address": "Sector 93, Noida",
        "established": "2017",
        "beneficiaries": "4,500+ meals daily",
        "website": "www.ckproject.org"
    },
    {
        "name": "Food Security Mission",
        "category": "Food",
        "description": "Working towards food security in urban slums.",
        "contact": "+91-9876543244",
        "email": "contact@fsm.org",
        "address": "Dilshad Garden, Delhi",
        "established": "2014",
        "beneficiaries": "12,000+ people monthly",
        "website": "www.fsm.org"
    },
    {
        "name": "Vastram Foundation",
        "category": "Clothes",
        "description": "Providing professional attire for job interviews.",
        "contact": "+91-9876543245",
        "email": "info@vastram.org",
        "address": "Sector 45, Noida",
        "established": "2016",
        "beneficiaries": "3,000+ job seekers equipped",
        "website": "www.vastram.org"
    },
    {
        "name": "Clothes For Change",
        "category": "Clothes",
        "description": "Recycling and upcycling clothes for sustainable fashion.",
        "contact": "+91-9876543246",
        "email": "help@clothesforchange.org",
        "address": "Shahdara, Delhi",
        "established": "2019",
        "beneficiaries": "15,000+ garments recycled",
        "website": "www.clothesforchange.org"
    },
    {
        "name": "Winter Care Initiative",
        "category": "Clothes",
        "description": "Distributing winter clothing to street dwellers.",
        "contact": "+91-9876543247",
        "email": "contact@wintercare.org",
        "address": "Shalimar Bagh, Delhi",
        "established": "2015",
        "beneficiaries": "7,000+ people supported",
        "website": "www.wintercare.org"
    },
    {
        "name": "Dress For Success Delhi",
        "category": "Clothes",
        "description": "Empowering women through professional clothing.",
        "contact": "+91-9876543248",
        "email": "delhi@dressforsuccess.org",
        "address": "Greater Kailash, Delhi",
        "established": "2017",
        "beneficiaries": "2,500+ women empowered",
        "website": "www.dressforsuccess.org"
    },
    {
        "name": "Textile Recycling Trust",
        "category": "Clothes",
        "description": "Sustainable textile recycling and distribution.",
        "contact": "+91-9876543249",
        "email": "info@textilerecycle.org",
        "address": "Sector 82, Noida",
        "established": "2018",
        "beneficiaries": "20,000+ kg textiles recycled",
        "website": "www.textilerecycle.org"
    },
    {
        "name": "Digital Education Hub",
        "category": "Education",
        "description": "Providing digital literacy to underprivileged youth.",
        "contact": "+91-9876543250",
        "email": "contact@digitalhub.org",
        "address": "Janakpuri, Delhi",
        "established": "2016",
        "beneficiaries": "5,000+ students trained",
        "website": "www.digitalhub.org"
    },
    {
        "name": "Science For All",
        "category": "Education",
        "description": "Making science education accessible and fun.",
        "contact": "+91-9876543251",
        "email": "info@scienceforall.org",
        "address": "Sector 41, Noida",
        "established": "2015",
        "beneficiaries": "10,000+ students reached",
        "website": "www.scienceforall.org"
    },
    {
        "name": "Language Learning Foundation",
        "category": "Education",
        "description": "Teaching English and foreign languages to underprivileged.",
        "contact": "+91-9876543252",
        "email": "help@llf.org",
        "address": "Preet Vihar, Delhi",
        "established": "2017",
        "beneficiaries": "4,000+ students enrolled",
        "website": "www.llf.org"
    },
    {
        "name": "Math Minds Initiative",
        "category": "Education",
        "description": "Making mathematics education accessible and enjoyable.",
        "contact": "+91-9876543253",
        "email": "contact@mathminds.org",
        "address": "Sector 22, Noida",
        "established": "2016",
        "beneficiaries": "6,000+ students benefited",
        "website": "www.mathminds.org"
    },
    {
        "name": "Creative Arts Education",
        "category": "Education",
        "description": "Promoting arts education in underprivileged communities.",
        "contact": "+91-9876543254",
        "email": "info@creativearts.org",
        "address": "Malviya Nagar, Delhi",
        "established": "2018",
        "beneficiaries": "3,500+ children enrolled",
        "website": "www.creativearts.org"
    },
    {
        "name": "Career Guidance Foundation",
        "category": "Education",
        "description": "Providing career counseling and guidance to students.",
        "contact": "+91-9876543255",
        "email": "help@cgf.org",
        "address": "Sector 12, Noida",
        "established": "2015",
        "beneficiaries": "8,000+ students guided",
        "website": "www.cgf.org"
    },
    {
        "name": "Women's Education Trust",
        "category": "Education",
        "description": "Focused on women's education and empowerment.",
        "contact": "+91-9876543256",
        "email": "contact@wet.org",
        "address": "Rajouri Garden, Delhi",
        "established": "2014",
        "beneficiaries": "5,500+ women educated",
        "website": "www.wet.org"
    },
    {
        "name": "Early Learning Initiative",
        "category": "Education",
        "description": "Focus on early childhood education in slum areas.",
        "contact": "+91-9876543257",
        "email": "info@eli.org",
        "address": "Sector 137, Noida",
        "established": "2017",
        "beneficiaries": "2,000+ children enrolled",
        "website": "www.eli.org"
    },
    {
        "name": "Technical Skills Foundation",
        "category": "Education",
        "description": "Providing technical and vocational training.",
        "contact": "+91-9876543258",
        "email": "contact@techskills.org",
        "address": "Vaishali, Ghaziabad",
        "established": "2016",
        "beneficiaries": "7,000+ students trained",
        "website": "www.techskills.org"
    },
    {
        "name": "Rural School Project",
        "category": "Education",
        "description": "Supporting education in rural areas around Delhi-NCR.",
        "contact": "+91-9876543259",
        "email": "help@ruralschool.org",
        "address": "Loni, Ghaziabad",
        "established": "2015",
        "beneficiaries": "4,500+ rural students",
        "website": "www.ruralschool.org"
    },
    {
        "name": "Sports Education Trust",
        "category": "Education",
        "description": "Promoting sports education and physical literacy.",
        "contact": "+91-9876543260",
        "email": "info@sportsedu.org",
        "address": "Vasant Kunj, Delhi",
        "established": "2018",
        "beneficiaries": "3,000+ children trained",
        "website": "www.sportsedu.org"
    },
    {
        "name": "Environmental Education Hub",
        "category": "Education",
        "description": "Teaching environmental awareness and sustainability.",
        "contact": "+91-9876543261",
        "email": "contact@enviro-edu.org",
        "address": "Sector 50, Noida",
        "established": "2017",
        "beneficiaries": "9,000+ students reached",
        "website": "www.enviro-edu.org"
    },
    {
        "name": "Music Education Society",
        "category": "Education",
        "description": "Providing music education to underprivileged children.",
        "contact": "+91-9876543262",
        "email": "info@musicedu.org",
        "address": "Laxmi Nagar, Delhi",
        "established": "2016",
        "beneficiaries": "1,500+ students trained",
        "website": "www.musicedu.org"
    },
    {
        "name": "Special Skills Center",
        "category": "Education",
        "description": "Vocational training for differently-abled individuals.",
        "contact": "+91-9876543263",
        "email": "help@specialskills.org",
        "address": "Sector 110, Noida",
        "established": "2015",
        "beneficiaries": "2,000+ individuals trained",
        "website": "www.specialskills.org"
    },
    {
        "name": "Youth Development Foundation",
        "category": "Education",
        "description": "Comprehensive youth development programs.",
        "contact": "+91-9876543264",
        "email": "contact@ydf.org",
        "address": "Krishna Nagar, Delhi",
        "established": "2017",
        "beneficiaries": "5,500+ youth mentored",
        "website": "www.ydf.org"
    }
]

# User session data (in-memory for demo purposes)
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('search'))
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password
            session['user'] = username
            return redirect(url_for('search'))
        else:
            return "Username already exists, please log in."
    return render_template('signup.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    results = []
    if request.method == 'POST':
        category = request.form.get('category')
        location = request.form.get('location')
        if category and location:
            results = [ngo for ngo in ngos if ngo['category'] == category and ngo['address'].endswith(location)]
    
    return render_template('search_results.html', results=results) if request.method == 'POST' else render_template('search.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
