import threading
import time

def added_thread_job():
	print('This is an added thread!')
	time.sleep(1)
	print('Added thread finished!')
def main():
	added_thread = \
	threading.Thread(target = added_thread_job)	# create thread		target:the thread's func args:the func's args
	# print(threading.active_count())		# thread count
	# print(threading.enumerate())		# thread list
	# print(threading.current_thread())	# this thread
	added_thread.setDaemon(True)		# !stop while the main thread stop
	added_thread.start()
	# thread.join()				# the other thread will wait until the thread finished.
	print("Over")


if __name__ == '__main__':
	main()
