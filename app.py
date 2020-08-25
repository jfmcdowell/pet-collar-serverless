#!/usr/bin/env python3

from aws_cdk import core

from pet_collar_gps.pet_collar_gps_stack import PetCollarGpsStack

app = core.App()
PetCollarGpsStack(app, "pet-collar-gps")

app.synth()
