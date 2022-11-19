from proto.iis_pb2_grpc import SimsInventoryInformationSystemServicer


class BackendServer(SimsInventoryInformationSystemServicer):
    def CreateUser(self, request, context):
        return super().CreateUser(request, context)

    def ReadUser(self, request, context):
        return super().ReadUser(request, context)

    def DeleteUser(self, request, context):
        return super().DeleteUser(request, context)

    def CreateShelf(self, request, context):
        return super().CreateShelf(request, context)

    def ReadShelf(self, request, context):
        return super().ReadShelf(request, context)

    def UpdateShelf(self, request, context):
        return super().UpdateShelf(request, context)

    def DeleteShelf(self, request, context):
        return super().DeleteShelf(request, context)

    def CreateSlot(self, request, context):
        return super().CreateSlot(request, context)

    def ReadSlot(self, request, context):
        return super().ReadSlot(request, context)

    def UpdateSlot(self, request, context):
        return super().UpdateSlot(request, context)

    def DeleteSlot(self, request, context):
        return super().DeleteSlot(request, context)

    def CreateSlots(self, request, context):
        return super().CreateSlots(request, context)

    def CreateItem(self, request, context):
        return super().CreateItem(request, context)

    def ReadItem(self, request, context):
        return super().ReadItem(request, context)

    def UpdateItem(self, request, context):
        return super().UpdateItem(request, context)

    def DeleteItem(self, request, context):
        return super().DeleteItem(request, context)


if __name__ == '__main__':
    print("Hello, World!")
