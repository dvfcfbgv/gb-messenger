import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .schemas.queries import ChatroomMembershipFilter, ChatroomMembershipNode
from .schemas.mutations import CreateChatroomMembership, DeleteChatroomMembership
from .schemas.subscriptions import ChatroomMembershipSubscriptions
from .models import ChatroomMembership as ChatroomMembershipModel


class Query(graphene.ObjectType):
    chatroom_membership = graphene.Field(
        ChatroomMembershipNode, unique_identifier=graphene.String(required=True))
    chatroom_memberships = DjangoFilterConnectionField(
        ChatroomMembershipNode, filterset_class=ChatroomMembershipFilter)

    def resolve_chatroom_membership(self, info, unique_identifier):
        return ChatroomMembershipModel.objects.get(unique_identifier=unique_identifier)


class Mutation(graphene.ObjectType):
    create_chatroom_membership = CreateChatroomMembership.Field()
    delete_chatroom_membership = DeleteChatroomMembership.Field()


class Subscription(graphene.ObjectType):
    chatroom_membership_subscriptions = ChatroomMembershipSubscriptions.Field()
