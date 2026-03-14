#pragma once
#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <vector>
#include "utilities.h"

// Definition of a celestial body
struct Body {
    std::string name;
    double mass;
    double radius;
    double period;
    std::array<double, 3> position;
    std::array<double, 3> velocity;
};

class CelestialBody {
    protected:
        // Physical Constants
        static constexpr double G = 6.67408e-11;
        static constexpr double AU = 1.496e+11;
        static constexpr double DS = 24 * 60 * 60;

    public:
        // Common Celestial Bodies
        static const Body sun;
        static const Body mercury;
        static const Body venus;
        static const Body earth;
        static const Body mars;
        static const Body jupiter;
        static const Body saturn;
        static const Body uranus;
        static const Body neptune;
        static const Body pluto;
        static const std::array<Body, 10> commonBodies;

        // Display Methods
        static void displayCommonBodies();
        static void displayBodyInfo(Body body);

        // Body Generation Methods
        static Body chooseRandomCommonBody();
        static Body generateCustomBody();
        static Body generateRandomSingleBody();
        static std::array<Body, 2> generateRandomTwoBody();
        static std::array<Body, 3> generateRandomThreeBody();

        // Random Single Body Parameter Generation Methods
        static std::array<double, 2> generateRandomSingleBodyNumMethodParams();
        static std::array<double, 2> generateRandomSingleBodyProjectileIC();

        // Random Two Body Parameter Generation Methods
        static std::array<double, 2> generateRandomTwoBodyNumMethodParams(Body body1, Body body2);

        // Random Three Body Parameter Generation Methods
        static std::array<double, 2> generateRandomThreeBodyNumMethodParams(Body body1, Body body2, Body body3);

        // Random N Body Parameter Generation Methods
        static std::vector<Body> generateRandomNBody();
        static std::array<double, 2> generateRandomNBodyNumMethodParams(const std::vector<Body>& bodies);

        // Uniform Single Body Parameter Generation Methods
        static std::vector<std::pair<double, double>> generateUniformSingleBodyNumMethodParams(int spanBins, int stepBins, bool shuffle);
        static std::vector<std::pair<double, double>> generateUniformSingleBodyProjectileIC(int posBins, int velBins, bool shuffle);

        // Helper Methods
        static double earthYearsToSeconds(double years) {
            return years * 365.25 * DS;
        }

    private:
        // Uniform Single Body Helper Methods
        static std::vector<double> generateUniformSingleBodyProjectilePositions(int bins);
        static std::vector<double> generateUniformSingleBodyProjectileTimeSpan(int bins);
        static std::vector<double> generateUniformSingleBodyProjectileTimeStep(int bins);
        static std::vector<double> generateUniformSingleBodyProjectileVelocities(int bins);
};