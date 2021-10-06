#include <gtest/gtest.h>
#include <chrono>
#include <thread>


TEST(INTEGRATIONTEST_DEMO, IntegrationTestGtest)
{
    std::this_thread::sleep_for(std::chrono::milliseconds(5000));
    GTEST_SUCCEED();
    //GTEST_FAIL();
}