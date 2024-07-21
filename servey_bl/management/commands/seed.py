from django.core.management.base import BaseCommand
from faker import Faker
from servey_bl.models import *

class Command(BaseCommand):
    help = 'Seed the database with test data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create categories
        categories = []
        for _ in range(3):
            category = Category.objects.create(
                name=fake.word(),
                description=fake.text()
            )
            categories.append(category)

        # Create question options
        options = []
        for _ in range(10):
            option = QuestionOption.objects.create(
                label=fake.sentence()
            )
            options.append(option)

        # Create questions
        questions = []
        for _ in range(5):
            question = Question.objects.create(
                label=fake.sentence()
            )
            question.options.set(options)
            questions.append(question)

        # Create steps
        steps = []
        for _ in range(3):
            step = Step.objects.create(
                name=fake.word(),
                description=fake.text()
            )
            step.questions.set(questions)
            steps.append(step)

        # Create surveys
        for _ in range(2):
            survey = Survey.objects.create(
                name=fake.word(),
                description=fake.text(),
                category=fake.random_element(categories)
            )
            survey.steps.set(steps)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with test data'))
