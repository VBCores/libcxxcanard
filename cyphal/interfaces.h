#pragma once

template <typename T>
class IListener {
public:
    virtual void accept(T) = 0;
};