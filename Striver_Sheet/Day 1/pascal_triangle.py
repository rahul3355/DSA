def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        if numRows == 0:
            return triangle

        for i in range(numRows):
            rows = []

            #first_element
            rows.append(1)

            #middle_element
            if i > 0:
                prev_row = triangle[i - 1]
                for j in range(1, i):
                    rows.append(prev_row[j - 1] + prev_row[j])

            #last_element
            if i > 0:
                rows.append(1)

            triangle.append(rows)

        return triangle