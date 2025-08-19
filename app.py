from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
import os
from datetime import datetime
from dotenv import load_dotenv
from server.webhooks import webhook_bp
from server import create_app

load_dotenv()

app = create_app()
csrf = CSRFProtect(app)

# Company information
COMPANY_INFO = {
    'name': 'Cuba Educational Travel',
    'abbreviation': 'CET',
    'tagline': 'With decades of experience and a dynamic team on the ground, CET produces unforgettable programs, from family trips to academic travel to corporate retreats.',
    'mission': 'Cuba Educational Travel is a team of young Cubans and Americans working together to help better the relationship between our two countries through legal travel, exchanges, and unforgettable experiences.',
    'founder': 'Collin Laverty, a leading expert on U.S.-Cuba relations',
    'legal_status': 'CET is legal and licensed by the Cuban and US governments',
    'email': 'info@cubaeducationaltravel.com',
    'phone': '+1 (202) 450-3321',
    'address': '1627 K Street NW, Suite 300, Washington, DC 20006',
    'founded': '2009'
}

# Navigation structure
NAVIGATION = {
    'cuba_travel': [
        {'name': 'People to People', 'url': 'travel_people_to_people'},
        {'name': 'Private Trips', 'url': 'travel_private'},
        {'name': 'Academic Programs', 'url': 'travel_academic'},
        {'name': 'CET Luxury', 'url': 'travel_luxury'},
        {'name': 'Corporate Travel', 'url': 'travel_corporate'},
        {'name': 'Events in Cuba', 'url': 'travel_events'}
    ],
    'about_cet': [
        {'name': 'The CET Story', 'url': 'about_story'},
        {'name': 'Impact', 'url': 'about_impact'},
        {'name': 'In the News', 'url': 'about_news'},
        {'name': 'Testimonials', 'url': 'about_testimonials'}
    ],
    'resources': [
        {'name': 'Business in Cuba', 'url': 'resources_business'},
        {'name': 'FAQs', 'url': 'resources_faqs'},
        {'name': 'Contact Us', 'url': 'contact'},
        {'name': 'The Newsletter', 'url': 'newsletter'}
    ]
}

# Sample testimonials
TESTIMONIALS = [
    {
        'name': 'Richard Feinberg',
        'title': 'Professor, UCSB, and author of Cuba: Open for Business',
        'quote': 'If you want to get to know Cuba from the inside out…if you want to experience the authentic, down-to-earth Cuba…if you want to create beautiful memories for a lifetime, here\'s your solution: visit Cuba with CET! For the first-class professionals at Cuba Educational Travel, tourism is so much more than a job, it\'s a moral commitment to building lasting bonds between international visitors and their many wonderful friends and colleagues in their beloved Cuba.'
    },
    {
        'name': 'James Williams',
        'title': 'President, Engage Cuba',
        'quote': 'CET\'s incredible team and on-the-ground knowledge is critically important to Engage Cuba and everyone who cares about U.S.-Cuba relations. Their real-time insights are essential to the policy discussions in D.C. and Havana.'
    },
    {
        'name': 'Sara Egozi',
        'title': 'MBA/MPA Candidate at Stanford GSB and Harvard Kennedy School',
        'quote': 'We partnered with CET to plan an educational trek for Harvard Kennedy School students and several cultural trips for Stanford Business School students. They offer the highest quality network across political and business communities in Cuba. As a Cuban American, I wanted a rich, diverse experience -- and CET delivered.'
    },
    {
        'name': 'Meg Crahan',
        'title': 'Senior Research Scholar and Director of the Cuba Program at Columbia University',
        'quote': 'Having travelled to Cuba dozens of times since 1973 for academic research, I was very familiar with the challenges involved. Cuba Educational Travel eliminates most of the hurdles for academic, cultural and scientific exchanges and is particularly astute in designing tailor-made programs to accommodate a wide variety of interests. CET combines professionalism with know-how.'
    },
    {
        'name': 'Mitchell C. Benson, M.D.',
        'title': 'President, NY Section AUA',
        'quote': 'The New York Section of the American Urological Association has an annual meeting every year. This year, we chose to have our meeting in Havana Cuba, jointly with the Cuban Urologic Association. This year\'s meeting in Cuba was an unforgettable experience and could not have been successful without the onsite assistance of CET.'
    },
    {
        'name': 'Mike Evans',
        'title': 'Founder of Full Court Peace, over 30 trips to Cuba',
        'quote': 'Cuba Educational Travel provides me with reliable counsel, proven advice and amazing general support. They know Cuba in and out, from safety to genuine grassroots experiences. I trust their guidance and expertise more than any other group involved in Cuba travel.'
    },
    {
        'name': 'Mario Recchia',
        'title': 'WorldPac Senior VP',
        'quote': 'I want to thank the CET team for making this a very memorable event for all our guests. The personal attention from arrival, all the activities, meals, discussions and the ultimate departure was flawlessly executed and greatly appreciated by all.'
    }
]

# FAQ data
FAQS = [
    {
        'question': 'Is travel to Cuba legal for US citizens?',
        'answer': 'Yes, Cuba Educational Travel is fully licensed by both Cuban and US governments to facilitate legal travel to Cuba under various categories including Support for the Cuban People and Educational Activities.'
    },
    {
        'question': 'What is included in CET programs?',
        'answer': 'Our programs include accommodation, meals, ground transportation, licensed guide services, entrance fees to sites, and all activities specified in the itinerary. International airfare is typically not included unless specified.'
    },
    {
        'question': 'What is the minimum group size?',
        'answer': 'There is no minimum number of participants for our private trips. Our groups range from two to two hundred participants.'
    },
    {
        'question': 'Can you customize trips?',
        'answer': 'Absolutely! We specialize in creating tailor-made programs focusing on different aspects of Cuban society including agriculture, arts and music, cuisine, education, environment, health care, fashion, science and sports.'
    },
    {
        'question': 'How far in advance should we book?',
        'answer': 'We recommend booking at least 60-90 days in advance to ensure availability and proper planning. However, we can sometimes accommodate shorter notice requests depending on group size and travel dates.'
    },
    {
        'question': 'What documents do I need to travel to Cuba?',
        'answer': 'U.S. citizens need a valid passport and a Cuban tourist visa (available through our office). We handle all the paperwork and ensure compliance with current U.S. regulations.'
    },
    {
        'question': 'What should I expect from the weather in Cuba?',
        'answer': 'Cuba has a tropical climate with warm temperatures year-round. The dry season (November-April) offers the most comfortable weather, while the wet season (May-October) can be humid with occasional afternoon showers.'
    },
    {
        'question': 'Is Cuba safe for American travelers?',
        'answer': 'Cuba is generally very safe for tourists. The country has low crime rates, and our local team provides 24/7 support throughout your trip to ensure your safety and comfort.'
    }
]

# Context processor to make data available in all templates
@app.context_processor
def inject_global_data():
    return {
        'company_info': COMPANY_INFO,
        'navigation': NAVIGATION,
        'testimonials': TESTIMONIALS,
        'current_year': datetime.now().year
    }

# Main routes
@app.route('/')
def index():
    """Homepage"""
    return render_template('index.html')

# Cuba Travel routes
@app.route('/cuba-travel/people-to-people')
def travel_people_to_people():
    """People to People Programs"""
    return render_template('cuba_travel/people_to_people.html')

@app.route('/cuba-travel/private-trips')
def travel_private():
    """Private Trips"""
    themes = ['agriculture', 'arts and music', 'cuisine', 'education', 
             'environment', 'health care', 'fashion', 'science', 'sports']
    return render_template('cuba_travel/private_trips.html', themes=themes)

@app.route('/cuba-travel/academic-programs')
def travel_academic():
    """Academic Programs"""
    return render_template('cuba_travel/academic_programs.html')

@app.route('/cuba-travel/cet-luxury')
def travel_luxury():
    """CET Luxury"""
    return render_template('cuba_travel/cet_luxury.html')

@app.route('/cuba-travel/corporate-travel')
def travel_corporate():
    """Corporate Travel"""
    return render_template('cuba_travel/corporate_travel.html')

@app.route('/cuba-travel/events-in-cuba')
def travel_events():
    """Events in Cuba"""
    return render_template('cuba_travel/events_cuba.html')

# About CET routes
@app.route('/about/the-cet-story')
def about_story():
    """The CET Story"""
    return render_template('about/story.html')

@app.route('/about/impact')
def about_impact():
    """Our Impact"""
    return render_template('about/impact.html')

@app.route('/about/in-the-news')
def about_news():
    """In the News"""
    return render_template('about/news.html')

@app.route('/about/testimonials')
def about_testimonials():
    """Testimonials"""
    return render_template('about/testimonials.html')

# Resources routes
@app.route('/resources/business-in-cuba')
def resources_business():
    """Business in Cuba"""
    return render_template('resources/business.html')

@app.route('/resources/faqs')
def resources_faqs():
    """FAQs"""
    return render_template('resources/faqs.html', faqs=FAQS)

@app.route('/resources/newsletter')
def newsletter():
    """Newsletter"""
    return render_template('resources/newsletter.html')

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact Us"""
    if request.method == 'POST':
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')

        if not all([first_name, last_name, email, message]):
            flash('Please fill in all required fields.', 'error')
            return render_template('contact.html')

        # In production, integrate with email service or database
        flash(f'Thank you {first_name}! Your message has been received. We will contact you soon at {email}.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

# Blog route
@app.route('/blog')
def blog():
    """The Cuba Blog"""
    return render_template('blog.html')

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5600)
