
def count_batteries_by_health(present_capacities):
  #Edge case 1: Checking if present_capacities is empty
  if(len(present_capacities)==0):
    print("No battery capacities passed!!")
  battery_rated_capacity=120    # All batteries have a rated capacity of 120Ah
  state_of_health,healthy_batteries,exchange_batteries,failed_batteries=0,0,0,0

  #Edge case 2: In case battery_rated_capacity is passed as a parameter to the function, it needs to be checked for zero
  if(battery_rated_capacity!=0):
    for battery_capacity in present_capacities:

        #Edge case 3: Battery capacity must not be negative
        if(battery_capacity>=0):
            state_of_health=(battery_capacity/battery_rated_capacity)*100   # Calculating state_of_health using the given formula

            #Checking appropriate conditions and classifying the batteries
            if 80<state_of_health<=100:
                healthy_batteries+=1

            elif 62<=state_of_health<=80:
                exchange_batteries+=1

            else:
                failed_batteries+=1
        else:
           print("Battery capacities cannot be negative!!")
  else:
     print("Battery rated capacity cannot be zero!!")
      
  return {
    "healthy": healthy_batteries,
    "exchange": exchange_batteries,
    "failed": failed_batteries
  }


def test_bucketing_by_health():
  print("Counting batteries by state_of_health...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)

  # Checking the function by passing empty present_capacities
  empty_capacity=count_batteries_by_health([])
  assert empty_capacity == {"healthy":0,"exchange":0,"failed":0}
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
