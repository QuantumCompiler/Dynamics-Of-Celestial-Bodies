#include <chrono>
#include <cstdint>
#include <iomanip>
#include <iostream>

double count_to(std::uint64_t n, std::uint64_t progress_every = 50'000'000ULL) {
    using clock = std::chrono::steady_clock;
    const auto start = clock::now();
    std::uint64_t i = 0;
    while (i < n) {
        ++i;
        if (progress_every && (i % progress_every == 0)) {
            const auto now = clock::now();
            const std::chrono::duration<double> elapsed = now - start;

            std::cout << "Reached " << i << " / " << n
                    << "  (elapsed: " << std::fixed << std::setprecision(2)
                    << elapsed.count() << "s)\n";
            std::cout.flush();
        }
    }
    const auto end = clock::now();
    const std::chrono::duration<double> elapsed = end - start;
    return elapsed.count();
}

int main() {
    const std::uint64_t n = 1'000'000'000ULL;
    std::cout << "Counting to " << n << "...\n";
    const double elapsed = count_to(n);
    std::cout << "Done. Elapsed time: " << std::fixed << std::setprecision(6)
            << elapsed << " seconds\n";
    return 0;
}