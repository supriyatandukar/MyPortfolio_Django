from django.core.management.base import BaseCommand
from core.models import Domain, Project, SkillGroup, Skill, Certification


class Command(BaseCommand):
    help = "Seeds the database with Supriya's projects, skills, and certifications"

    def handle(self, *args, **kwargs):
        # Domains 
        cv_domain, _ = Domain.objects.get_or_create(name='Computer Vision', defaults={'slug': 'computer-vision'})
        ml_domain, _ = Domain.objects.get_or_create(name='Machine Learning', defaults={'slug': 'machine-learning'})
        nlp_domain, _ = Domain.objects.get_or_create(name='NLP & AI', defaults={'slug': 'nlp-ai'})
        data_domain, _ = Domain.objects.get_or_create(name='Data Engineering', defaults={'slug': 'data-engineering'})

        # Projects 
        projects_data = [
            {
                'title': 'NagarConnect',
                'slug': 'nagarconnect',
                'tagline': 'Smart community issue reporting and priority-based management',
                'description': 'Built an NLP pipeline (TF-IDF and Logistic Regression) to classify community complaints and route them by priority and department. Added keyword and location extraction to turn unstructured complaint text into actionable data.',
                'domain': nlp_domain,
                'tech_stack': 'Python, NLP, Scikit-learn',
                'github_url': 'https://github.com/supriyatandukar/nagarconnect-community',
                'featured': True,
            },
            {
                'title': 'Rice Classification System',
                'slug': 'rice-classification',
                'tagline': 'Image classification to identify rice varieties',
                'description': 'Built and compared image classification models (Scikit-learn vs. MobileNetV2 transfer learning) to identify rice varieties. Preprocessed image data and evaluated model performance to select the most effective approach.',
                'domain': cv_domain,
                'tech_stack': 'Python, TensorFlow, Scikit-learn, MobileNetV2',
                'github_url': 'https://github.com/supriyatandukar/rice-classification',
                'featured': False,
            },
            {
                'title': 'Exoplanet Detection Model',
                'slug': 'exoplanet-detection',
                'tagline': 'Binary classification to detect potential exoplanets',
                'description': 'Built a binary classification model to detect potential exoplanets using the NASA Kepler dataset. Evaluated performance using accuracy and confusion matrix analysis.',
                'domain': ml_domain,
                'tech_stack': 'Python, Scikit-learn, Machine Learning',
                'github_url': 'https://github.com/supriyatandukar/exoplanet-detection',
                'featured': False,
            },
            {
                'title': 'Fraud Detection System',
                'slug': 'fraud-detection',
                'tagline': 'Identifying fraudulent transaction patterns at scale',
                'description': 'Processed large transaction datasets with PySpark and Hive to identify patterns of fraudulent activity. Applied data-processing techniques to convert raw transaction data into actionable insights.',
                'domain': data_domain,
                'tech_stack': 'Python, PySpark, Hive',
                'github_url': 'https://github.com/supriyatandukar/fraud-detection',
                'featured': False,
            },
            {
                'title': 'BhasaBelle',
                'slug': 'bhasabelle',
                'tagline': 'AI-powered language assistant',
                'description': 'Built an AI language assistant for translation, summarization, and sentiment analysis using the Gemini API. Developed FastAPI backend services to connect AI functionality with the application.',
                'domain': nlp_domain,
                'tech_stack': 'Python, Gemini API, FastAPI, HTML, CSS, JavaScript',
                'github_url': 'https://github.com/supriyatandukar/bhasabelle',
                'featured': True,
            },
            {
                'title': 'Spotify Music Recommendation System',
                'slug': 'spotify-recommender',
                'tagline': 'Recommending music using audio feature similarity',
                'description': 'Built a music recommender using audio features (tempo, energy, danceability) and cosine similarity.',
                'domain': ml_domain,
                'tech_stack': 'Python, Scikit-learn',
                'github_url': 'https://github.com/supriyatandukar/spotify-recommender',
                'featured': False,
            },
            {
                'title': 'Market Basket Analysis',
                'slug': 'market-basket-analysis',
                'tagline': 'Uncovering product associations for cross-selling',
                'description': 'Applied the Apriori algorithm to retail transaction data to uncover product associations for cross-selling.',
                'domain': data_domain,
                'tech_stack': 'Python, Apriori, Data Mining',
                'github_url': 'https://github.com/supriyatandukar/market-basket-analysis',
                'featured': False,
            },
        ]

        for data in projects_data:
            slug = data.pop('slug')
            obj, created = Project.objects.get_or_create(slug=slug, defaults={**data, 'slug': slug})
            status = 'Created' if created else 'Already exists'
            self.stdout.write(self.style.SUCCESS(f"{status}: {obj.title}"))

        # Skills 
        skills_data = {
            'Programming & Data': ['Python', 'SQL', 'Pandas', 'NumPy', 'Excel'],
            'Machine Learning': ['Scikit-learn', 'Classification', 'Clustering', 'Association Rules', 'Feature Engineering'],
            'Deep Learning & AI': ['TensorFlow', 'Keras', 'NLP', 'TF-IDF', 'MediaPipe', 'Gemini API'],
            'Data Processing': ['PySpark', 'Hive', 'Data Cleaning', 'Exploratory Data Analysis'],
            'Visualization': ['Tableau', 'Power BI', 'Matplotlib'],
            'Backend & Deployment': ['FastAPI', 'REST APIs', 'Docker'],
            'Tools': ['Git', 'GitHub', 'VS Code'],
        }

        for i, (group_name, skill_list) in enumerate(skills_data.items()):
            group, _ = SkillGroup.objects.get_or_create(name=group_name, defaults={'order': i})
            for j, skill_name in enumerate(skill_list):
                Skill.objects.get_or_create(name=skill_name, group=group, defaults={'order': j})
            self.stdout.write(self.style.SUCCESS(f"Seeded skill group: {group_name}"))

        # Certifications
        cert_names = [
            'Introduction to Data Science',
            'AI Literacy for All',
            'Introduction to MS Excel',
            'AWS Cloud Practitioner Essentials',
        ]
        for i, name in enumerate(cert_names):
            Certification.objects.get_or_create(name=name, defaults={'order': i})
        self.stdout.write(self.style.SUCCESS("Seeded certifications"))

        self.stdout.write(self.style.SUCCESS("All done!"))