import logging


def create_logger():
    db_logger = logging.getLogger('db')
    return db_logger


# Calculate all Fibonacci numbers which are less than or equal to k.
def calc_list_numbers(fibo_nums, k, logger):
    if k > 1:
        i = 1
        fibo_nums.append(2)
    else:
        return

    if k > 2:
        fibo_nums.append(3)
        i = 2

    while True:

        next_term = (fibo_nums[i - 1] + fibo_nums[i - 2])

        # If next number is greater than k do not push it in vector and return.
        if next_term > k:
            logger.info('List of fibonacci numbers ' + fibo_nums.__str__() + ' created ')
            return

        fibo_nums.append(next_term)
        i += 1


# Find all the available sequences for the number k
def seq_fib(fibo_nums, k, inic, num, fibo_seq, logger):
    i = 0

    while i < len(fibo_nums):
        rest = k
        fibo_seq_aux = [inic]
        j = i
        if inic == num and fibo_nums.__contains__(inic) and not fibo_seq.__contains__(fibo_seq_aux):
            fibo_seq.append(fibo_seq_aux)
        while rest > 0 and j < len(fibo_nums):
            if rest >= fibo_nums[j] and rest - fibo_nums[j] != 1:
                rest -= fibo_nums[j]
                fibo_seq_aux.append(fibo_nums[j])
            else:
                j += 1
            if rest == 0:
                if not fibo_seq.__contains__(sorted(fibo_seq_aux)):
                    fibo_seq.append(sorted(fibo_seq_aux))
                    logger.info('Adding ' + sorted(fibo_seq_aux).__str__() + ' to the list of sequences')
                rest = k
                fibo_seq_aux = [inic]
                j += 1
        i += 1


# Function to find sequences of Fibonacci terms having sum equal to k.
def calc_seq(k):
    logger = create_logger()
    logger.info('Creating sequences for number ' + k.__str__() + '...')
    print('Creating sequences for number ' + k.__str__() + '...')

    try:
        k = int(k)
        # Vector to store Fibonacci numbers.
        fibo_nums = []
        fibo_seq = []
        calc_list_numbers(fibo_nums, k, logger)
        i = 0
        while i < len(fibo_nums):
            seq_fib(fibo_nums, k - fibo_nums[i], fibo_nums[i], k, fibo_seq, logger)
            i += 1

        if fibo_seq:
            logger.info('List of fibonacci sequences ' + fibo_seq.__str__() + ' successfully created')
        else:
            logger.info('There are no sequences for number ' + k.__str__())

        return sorted(fibo_seq)
    except Exception as e:
        logger.exception(e)

# Driver code
if __name__ == "__main__":
    k = 7
    print(calc_seq(k))
