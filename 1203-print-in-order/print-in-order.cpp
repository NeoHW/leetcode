class Foo {
public:
    Foo() : stage(1) {}

    void first(function<void()> printFirst) {
        std::unique_lock<std::mutex> lk{mtx};
        // we need to capture this as stage is a member variable, only accessible via this->stage
        cv.wait(lk, [this] {return stage == 1; });

        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        stage = 2;
        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        std::unique_lock<std::mutex> lk{mtx};
        cv.wait(lk, [this]{return stage == 2; });
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        stage = 3;
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        std::unique_lock<std::mutex> lk{mtx};
        cv.wait(lk, [this] { return stage == 3; });
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }

private:
    int stage;
    std::mutex mtx;
    std::condition_variable cv;
};