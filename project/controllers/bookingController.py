from flask import Flask, jsonify,request
from flask import render_template
from project.helpers.utility import sendResponse
from project.models.poolVillaModel import model
from project.repositories.bookingRepository import repository


class BookingController():

    def __init__(self):
        pass

    def getAllBooking(self,param):
        return repository.getAllBooking(param)

bookingController=BookingController()

