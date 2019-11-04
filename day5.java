// Simulation of random walks
// Stop when s(t) == 0 or s(t) == -k
// Calculate the probability of above
import java.util.*;
public class day5 {
    private static final int INITIAL_VALUE = -1;
    // private final int K = 3;
    private static final int TRIALS = 10000;
    public static void main(String[] args) {
        // Key as k, value as probablity
        Random rand = new Random();
        Map<Integer, Double> result = new TreeMap<>();
        for (int i = 1; i <= 1000; i++) {
            result.put(i, negKProbability(TRIALS, INITIAL_VALUE, i, rand));
        }
        System.out.println(result);
    }

    // sum is the sum of current random walk
    // -k is the aim bound, suppose k is positive
    // return 1 if sum is -k, 0 otherwise
    private static int walk(int sum, int k, Random rand) {
        if (sum == -k) {
            return 1;
        }
        if (sum == 0) {
            return 0;
        }
        int singleStep = rand.nextBoolean() ? 1 : -1;
        return walk(sum + singleStep, k, rand);
    }

    private static int iteWalk(int initial, int k, Random rand) {
        while(initial != -k && initial != 0) {
            initial += rand.nextBoolean() ? 1 : -1;
        }
        if (initial == -k) {
            return 1;
        }
        return 0;
    }

    // Return the probability of ending with -k
    private static double negKProbability(int trials, int intial, int k, Random rand) {
        double count = 0;
        for (int i = 0; i < trials; i++) {
            if (iteWalk(intial, k, rand) == 1) {
                count += 1;
            }
        }
        return (double)count/trials;
    }

}