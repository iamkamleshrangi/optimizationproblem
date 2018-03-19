from operator import itemgetter


class Optimiser():
    def loader(self, dataSet):
        print dataSet
        count = len(dataSet)
        dataSet = self.job_sort(dataSet)
        if count == 1:
            max_profit = dataSet[0][2]
            return max_profit
        else:
            return self.run(dataSet, count)

    def run(self, data_arr, count):
        if count == 1:
            max_profit = data_arr[0][2]
            return max_profit

        firstpro = data_arr[count - 1][2]
        noncon = self.notconflictcases(data_arr, count)
        if (noncon != -1):
            firstpro = firstpro + self.run(data_arr, (noncon + 1));
        extrapro = self.run(data_arr, count - 1);
        return max(firstpro, extrapro)

    def job_sort(self, data_arr):
        data_arr = sorted(data_arr, key=itemgetter(1))
        return data_arr

    def notconflictcases(self, data_arr, count):
        for i in range(count - 1, -1, -1):
            if (data_arr[i][1] <= data_arr[count - 1][0]):
                return i
        return -1


obj = Optimiser()
obj.loader([[0, 5, 10], [0, 7, 8], [5, 9, 7], [6, 9, 8], [2, 1, 500]])
