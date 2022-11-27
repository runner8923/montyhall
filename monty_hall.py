import random

TRIES = 10000

class MontyHallSim:

   def __init__(self, doors):
      self.doors = doors
      self.winCount = 0
      self.switchWinCount = 0
      self.attemptCount = 0;

   def pickDoor(self):
      return random.randint(1,self.doors)
      
   def pickInitialPlayer(self):
      return random.randint(1,self.doors)
      
   def pickNotDoor(self, pick, door):
      notDoor = random.randint(1,self.doors)
      
      while notDoor == pick or notDoor == door:
         notDoor = random.randint(1,self.doors)
      return notDoor
   
   def pickAgain(self, initialPick, notPick):
      pick = random.randint(1,self.doors)
      while pick == initialPick or pick == notPick:
         pick = random.randint(1,self.doors)
      return pick
         
   def run(self, tries):
      print("Running simulation") 
      for x in range(tries):
         self.attemptCount = self.attemptCount + 1
         door = self.pickDoor()
         playerPick = self.pickInitialPlayer()
         notDoor = self.pickNotDoor(playerPick, door)
         print("Pick: %d Door: %d" % (playerPick, door))
         print("It's not %d" % notDoor)
         if door == playerPick:
            self.winCount = self.winCount + 1
            
         newPick = self.pickAgain(playerPick, notDoor)
         if door == newPick:
            self.switchWinCount = self.switchWinCount + 1
            
      print("You won %d times out of %d (%f)" % (self.winCount, self.attemptCount, 100*self.winCount/float(self.attemptCount)))
      print("If you switched you would have won %d times out of %d (%f)" % (self.switchWinCount, self.attemptCount, 100*self.switchWinCount/float(self.attemptCount)))

sim = MontyHallSim(3)
sim.run(TRIES)