import random

def generate_processes(num_processes, mean_execution_time, std_dev_arrival_time,zero_arrival = False):
  # lista procesów
  processes = []
  # początkowy czas przyjścia

  # iterujemy po wszystkich procesach
  for i in range(num_processes):
    # losujemy czas przyjścia z rozkładu normalnego
    if zero_arrival:
      arrival_time = 0
    else:
      arrival_time = int(random.normalvariate(mean_execution_time, std_dev_arrival_time))
    # losujemy czas wykonywania z rozkładu normalnego
    execution_time = int(random.normalvariate(mean_execution_time, std_dev_arrival_time))
    # dodajemy proces do listy
    processes.append((abs(arrival_time), abs(execution_time)))

  return processes

def fcfs_scheduling(processes):
    # sortujemy procesy według czasu przybycia
    processes = sorted(processes, key=lambda x: x[0])
    for i, (arrival_time, execution_time) in enumerate(processes):
        print(f'p{i+1}',' : arrival time : ',arrival_time,' : execution time : ', execution_time)
    # inicjalizujemy zmienne
    current_time = 0
    waiting_times = []
    counter = 0
    # dla każdego procesu
    for i,(arrival_time, execution_time) in enumerate(processes):
        # obliczamy czas oczekiwania
        waiting_time = current_time - arrival_time
        waiting_times.append(waiting_time)
        # dodajemy czas wykonania procesu do bieżącego czasu
        current_time += execution_time
        counter += 1

    # obliczamy średni czas oczekiwania
    average_waiting_time = sum(waiting_times) / len(waiting_times)

    return (average_waiting_time, counter)

def lcfs_scheduling(processes):
    # sortujemy procesy według czasu przybycia
    processes = sorted(processes, key=lambda x: x[0], reverse=True)
    for i, (arrival_time, execution_time) in enumerate(processes):
        print(f'p{i+1}',' : arrival time : ',arrival_time,' : execution time : ', execution_time)
    # inicjalizujemy zmienne
    current_time = 0
    waiting_times = []
    counter = 0

    # dla każdego procesu
    for i,(arrival_time, execution_time) in enumerate(processes):
        # obliczamy czas oczekiwania
        waiting_time = current_time - arrival_time
        waiting_times.append(waiting_time)
        # dodajemy czas wykonania procesu do bieżącego czasu
        current_time += execution_time
        counter += 1
    # obliczamy średni czas oczekiwania
    average_waiting_time = sum(waiting_times) / len(waiting_times)

    return (average_waiting_time, counter)
#generator(ilosc, srednia, odchylenie standardowe, czy zerować = False)
generator_amount = 100
generator_mean = 10
generator_std_dev = 5
is_zero = False
processes = generate_processes(generator_amount,generator_mean,generator_std_dev, is_zero)
processes = sorted(processes, key=lambda x: x[0])
for process in processes:
    print(process, end=' ')
print()
#[(2,6),(5,2),(1,8),(0,3),(4,4)]
avg_time, time = fcfs_scheduling(processes)
avg_time2, time2 = lcfs_scheduling(processes)
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
with open(r'C:\Users\User\Documents\data_processing.txt', "a") as f:
    #f.write('\n' + output + '\n')
    f.write('\ngenerator amount: ' + str(generator_amount) + '\n')
    f.write('generator mean: ' + str(generator_mean) + '\n')
    f.write('generator standard deviation: ' + str(generator_std_dev) + '\n')
    f.write('arrival times: ' + arrival_output_str + '\n')
    f.write('execution times: ' + execution_output_str + '\n')
    f.write('average waiting time fcfs: ' + str(avg_time) + '\n')
    f.write('time in the loop fcfs: ' + str(time) + '\n')
    f.write('average waiting time lcfs: ' + str(avg_time2) + '\n')
    f.write('time in the loop lcfs: ' + str(time2) + '\n')

#dzien doberek

#print('\nsrednia arrival: ',sum(arrival_output)/len(arrival_output))
#print('\nsrednia execution: ',sum(execution_output)/len(execution_output))