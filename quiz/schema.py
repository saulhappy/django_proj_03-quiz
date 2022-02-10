import graphene
from graphene_django import DjangoObjectType, DjangoListField
from quiz.models import Quizzes, Category, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")

class Query(graphene.ObjectType):
    all_quizzes = graphene.Field(QuizzesType)
    all_questions = graphene.List(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_quizzes(root, info):
        return Quizzes.objects.all()

    def resolve_all_questions(root, info, id):
        return Question.objects.filter(pk=id)

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)


class CategoryMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryMutation(category=category)



class Mutation(graphene.ObjectType):

    update_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
