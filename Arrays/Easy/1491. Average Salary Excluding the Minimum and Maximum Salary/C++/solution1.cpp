class Solution {
public:
    double average(vector<int>& salaries) {
        int minSalary = INT_MAX;
        int maxSalary = 0;
        int sum = 0;
        for (int salary : salaries) {
            if (salary < minSalary) {
                minSalary = salary;
            }
            if (salary > maxSalary) {
                maxSalary = salary;
            }
            sum += salary;
        }
        return static_cast<double>(sum - minSalary - maxSalary) / (salaries.size() - 2);
    }
};
