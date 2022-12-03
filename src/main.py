from backend_proto.iis_pb2_grpc import SimsInventoryInformationSystemServicer
from db_operations import InventoryDB
from concurrent import futures

import backend_proto.iis_pb2_grpc as backend_grpc
import backend_proto.item_messages_pb2 as item_messages
import backend_proto.shelf_messages_pb2 as shelf_messages
import backend_proto.slot_messages_pb2 as slot_messages
import backend_proto.user_messages_pb2 as user_messages

import grpc
import time
import sqlite3
import logging
import secrets
from base64 import b64encode

class BackendServer(SimsInventoryInformationSystemServicer):
    def __init__(self):
        self.db = InventoryDB()

    def CreateUser(self, request, context):
        self.db.insert_user(request.info.user_id)
        return user_messages.CreateUserResponse()

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
        result = None
        returnList = []
        if request.item_id != 0:
            print("item id here")
            result = self.db.get_item(itemID=request.item_id,shelfID=None)
        else:
            if request.shelf_id != "":
                print("shelf id here")
                result = self.db.get_item(itemID=None,shelfID=request.shelf_id)
            else:
                print("item id here")
                result = self.db.get_item()

        if result is not None:
            for entry in result:
                returnList.append(item_messages.ItemInfo(description=entry[2],object_id=entry[0],shelf_id=entry[5],price=entry[3],stock=entry[1]))
            print(result,returnList)
        
        return item_messages.ReadItemResponse(info=returnList)

        return super().ReadItem(request, context)

    def UpdateItem(self, request, context):
        return super().UpdateItem(request, context)

    def DeleteItem(self, request, context):
        return super().DeleteItem(request, context)


if __name__ == '__main__':
    db = InventoryDB()
    #db.create_tables()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    backend_grpc.add_SimsInventoryInformationSystemServicer_to_server(BackendServer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Running")
    server.wait_for_termination()
