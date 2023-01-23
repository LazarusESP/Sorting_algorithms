import random
import csv

def generate_processes(num_processes, mean_execution_time, std_dev_execution_time, mean_arrival_time, std_dev_arrival_time, zero_arrival = False):
  # lista procesów
  processes = []
  # początkowy czas przyjścia

  # iterujemy po wszystkich procesach
  for i in range(num_processes):
    # losujemy czas przyjścia z rozkładu normalnego
    if zero_arrival:
      arrival_time = 0
    else:
      arrival_time = int(random.normalvariate(mean_arrival_time, std_dev_arrival_time))
    # losujemy czas wykonywania z rozkładu normalnego
    execution_time = int(random.normalvariate(mean_execution_time, std_dev_execution_time))
    # dodajemy proces do listy
    processes.append((abs(arrival_time), abs(execution_time)))

  return processes

def fcfs_scheduling(processes):
    # sortujemy procesy według czasu przybycia
    processes = sorted(processes, key=lambda x: x[0])
    for i, (arrival_time, execution_time) in enumerate(processes):
        print(f'p{i+1}',' : arrival time : ',arrival_time,' : execution time : ', execution_time)
    # inicjalizujemy zmienne
    completion_time = 0
    waiting_times = []
    turnaround_time = []
    counter = 0
    # dla każdego procesu
    for i,(arrival_time, execution_time) in enumerate(processes):
        completion_time += execution_time
        
        turnaround_time.append(completion_time - arrival_time)
        # obliczamy czas oczekiwania i turnaround time
        waiting_times.append(turnaround_time[i] - execution_time)
        # dodajemy czas wykonania procesu do bieżącego czasu
        counter += 1

    # obliczamy średni czas oczekiwania
    average_waiting_time = sum(waiting_times) / len(waiting_times)
    average_turnaround_time = sum(turnaround_time) / len(turnaround_time)

    return (average_waiting_time, average_turnaround_time, counter)

def lcfs_scheduling(processes):
    # sortujemy procesy według czasu przybycia
    processes = sorted(processes, key=lambda x: x[0], reverse=True)
    for i, (arrival_time, execution_time) in enumerate(processes):
        print(f'p{i+1}',' : arrival time : ',arrival_time,' : execution time : ', execution_time)
    # inicjalizujemy zmienne
    completion_time = 0
    waiting_times = []
    turnaround_time = []
    counter = 0

    # dla każdego procesu
    for i, (arrival_time, execution_time) in enumerate(processes):
        completion_time += execution_time
        turnaround_time.append(completion_time - arrival_time)
        waiting_times.append(turnaround_time[i] - execution_time)
        counter += 1

    # obliczamy średni czas oczekiwania
    average_waiting_time = sum(waiting_times) / len(waiting_times)
    average_turnaround_time = sum(turnaround_time) / len(turnaround_time)

    return (average_waiting_time, average_turnaround_time, counter)
#generator(ilosc, srednia execution, odchylenie standardowe execution,srednia arrival, odchylenie standardowe arrival,
#  czy zerować = False)
generator_amount = 10
execution_mean = 10
execution_std_dev = 5
arrival_mean = 20
arrival_std_dev = 2
is_zero = False
processes = generate_processes(generator_amount, execution_mean, execution_std_dev,arrival_mean, arrival_std_dev, is_zero)
processes = sorted(processes, key=lambda x: x[0])
for process in processes:
    print(process, end=' ')
print()
#[(2,6),(5,2),(1,8),(0,3),(4,4)]
avg_time, avg_turnaround, time = fcfs_scheduling(processes)
avg_time2, avg_turnaround2, time2 = lcfs_scheduling(processes)
print('średni czas oczekiwania fcfs: ', avg_time,'czas programu fcfs: ',time)
print('średni czas oczekiwania lcfs: ',avg_time2,'czas programu lcfs: ',time2)
#output = ' '.join(map(str,processes))
arrival_output = []
execution_output = []
for i, (arrival_time, execution_time) in enumerate(processes):
    arrival_output.append(arrival_time)
    execution_output.append(execution_time)
arrival_output_str = ' '.join(map(str,arrival_output))
execution_output_str = ' '.join(map(str,execution_output))

with open(r'C:\Users\Piotr\Documents\data_processing.csv', "a", newline = '') as csvfile:
    thewriter = csv.writer(csvfile)
    data = [generator_amount, avg_time, avg_time2,avg_turnaround , avg_turnaround2]
    thewriter.writerow(data)


#print('\nsrednia arrival: ',sum(arrival_output)/len(arrival_output))
#print('\nsrednia execution: ',sum(execution_output)/len(execution_output))