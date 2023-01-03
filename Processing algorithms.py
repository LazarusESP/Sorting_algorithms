import random

def generate_processes(num_processes, mean_execution_time, std_dev_arrival_time):
  # lista procesów
  processes = []
  # początkowy czas przyjścia

  # iterujemy po wszystkich procesach
  for i in range(num_processes):
    # losujemy czas przyjścia z rozkładu normalnego
    arrival_time = int(random.normalvariate(mean_execution_time, std_dev_arrival_time))
    # losujemy czas wykonywania z rozkładu normalnego
    execution_time = int(random.normalvariate(mean_execution_time, std_dev_arrival_time))
    # dodajemy proces do listy
    processes.append((arrival_time, execution_time))

  return processes

def fcfs_scheduling(processes):
    # sortujemy procesy według czasu przybycia
    processes = sorted(processes, key=lambda x: x[0])
    for i, (arrival_time, execution_time) in enumerate(processes):
        print(f'p{i+1}',' : arrival time : ',arrival_time,' : execution time : ', execution_time)
    # inicjalizujemy zmienne
    current_time = 0
    waiting_times = []

    # dla każdego procesu
    for i,(arrival_time, execution_time) in enumerate(processes):
        # obliczamy czas oczekiwania
        waiting_time = current_time - arrival_time
        waiting_times.append(waiting_time)
        # dodajemy czas wykonania procesu do bieżącego czasu
        current_time += execution_time

    # obliczamy średni czas oczekiwania
    average_waiting_time = sum(waiting_times) / len(waiting_times)

    return average_waiting_time

def lcfs_scheduling(processes):
    # sortujemy procesy według czasu przybycia
    processes = sorted(processes, key=lambda x: x[0], reverse=True)
    for i, (arrival_time, execution_time) in enumerate(processes):
        print(f'p{i+1}',' : arrival time : ',arrival_time,' : execution time : ', execution_time)
    # inicjalizujemy zmienne
    current_time = 0
    waiting_times = []

    # dla każdego procesu
    for i,(arrival_time, execution_time) in enumerate(processes):
        # obliczamy czas oczekiwania
        waiting_time = current_time - arrival_time
        waiting_times.append(waiting_time)
        # dodajemy czas wykonania procesu do bieżącego czasu
        current_time += execution_time

    # obliczamy średni czas oczekiwania
    average_waiting_time = sum(waiting_times) / len(waiting_times)

    return average_waiting_time

processes = generate_processes(5,10,3)#[(2,6),(5,2),(1,8),(0,3),(4,4)]
average_waiting_time = fcfs_scheduling(processes)
print('średni czas oczekiwania: ', average_waiting_time)