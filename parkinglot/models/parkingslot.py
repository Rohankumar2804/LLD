from parkinglot.models.car import Car
from parkinglot.models.slot import Slot
from parkinglot.strategy.parking_strategy import ParkingStrategy


class ParkingLot:
      def __init__(self,capacity,strategy:ParkingStrategy):
          self.slots = [Slot(i) for i in range(capacity)]
          self.strategy = strategy
          self.strategy.add_slots(self.slots)

      def park(self,car:Car):
          slot = self.strategy.get_next_available_slot()
          if slot:
              slot.park_car(car)
          # raise
      def leave(self,slot_number):
          if slot_number < len(self.slots):
            self.slots[slot_number].leave()
            self.strategy.add_slot(self.slots[slot_number])

      def getStatus(self):
          return [(slot.get_number(),slot.get_parked_car().get_registration_number(),slot.get_parked_car().get_color()) for slot in self.slots if not slot.is_free()]

      def get_slot_by_reg(self, reg_number):
          for slot in self.slots:
              if not slot.is_free() and slot.get_parked_car().get_registration_number() == reg_number:
                  return slot.get_number()
          return None

      def get_slots_by_color(self, color):
          return [s.get_number() for s in self.slots if not s.is_free() and s.get_parked_car().get_color().lower() == color.lower()]

      def get_regs_by_color(self, color):
          return [s.get_parked_car().get_registration_number() for s in self.slots if not s.is_free() and s.get_parked_car().color.lower() == color.lower()]