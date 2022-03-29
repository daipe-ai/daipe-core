import inspect
from daipecore.decorator.StringableParameterInterface import StringableParameterInterface
from injecta.parameter.all_placeholders_replacer import find_all_placeholders, replace_all_placeholders
from injecta.container.ContainerInterface import ContainerInterface


class InstanceMembersTransformer:
    def transform_members(self, instance, container: ContainerInterface):
        for member in self.__get_transformable_members(instance):
            instance.__setattr__(member[0], self.__transform_member(member[1], container))

    def __transform_member(self, member, container: ContainerInterface):  # noqa
        return replace_all_placeholders(member, find_all_placeholders(member), container.get_parameters(), member)

    def __get_transformable_members(self, instance):  # noqa
        transformable_members = []

        for member in inspect.getmembers(instance):
            if isinstance(member[1], StringableParameterInterface) and find_all_placeholders(member[1].to_string()):
                transformable_members.append((member[0], member[1].to_string()))

            if isinstance(member[1], str) and find_all_placeholders(member[1]):
                transformable_members.append((member[0], member[1]))

        return transformable_members
