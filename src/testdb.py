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

testdb = InventoryDB()
testdb.insert_user("usertest")
# testdb.insert_shelf("shelf1", 12, "usertest")
# testdb.insert_slot(1,20,0,"shelf1")
# testdb.insert_item(1223,10,"test object",10.5,1,"shelf1")
