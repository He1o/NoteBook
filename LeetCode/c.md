### 1. 数值
```
int a; //1258249841
```
int不赋初值的话，a可能是任意值 

### 1. 字符串

单个字母应该用'a'，"a" 则表示为字符串

单引号对包括的只能是单个字母，表示一个字母，没有其它任何东西。在存储器中只占用存放一个字母所需的空间。 

双引号对包括的是一个字符串，字符串的结尾必须以'\0'字符(数值0)作为结尾标志。如果包括的是单个字母，表示这个字符串只有一个字母成员，再包括末尾的'\0'字符(数值0)作为结尾标志，这样在存储器中实际占用存放两个字母所需的空间。

string和vector一样都有 push_back 和 pop_back

### 2. 定义数组
```
int a[] = {2, 3, 4}
```

### 2. 定义哈希表
1. 定义
```
unordered_map<string, int> hashtable = {
    {key1, val1},
    {key2, val2}
}
```
2. hashtable.count(key) 对key进行计数，如果存在则为1，不存在则为0，最大为1.
3. 当使用[]调用键值对时，如没有则会在其中添加，如果值的类型为int，则默认值为0

4. 遍历方式
```
    // 方式一、迭代器
    cout << "方式一、迭代器" << endl;
    for (auto it = mp.begin(); it != mp.end(); it++) {
        cout << it -> first << " " << it -> second << endl;
    }

    // 方式二、range for C++ 11版本及以上
    cout << "\n方法二、 range for" << endl;
    for (auto it : mp) {
        cout << it.first << " " << it.second << endl;
    }

    // 方法三、 C++ 17版本及以上  结构化绑定
    cout << "\n方法三" << endl;
    for (auto [key, val] : mp) {
        cout << key  << " " << val << endl;
    }
```

### 5. 栈
```
stack<int> stk;
stk.push(); //存入
stk.pop(); 
stk.top();
```

### share_ptr
```
shared_ptr<vector<string>>(new vector<string>{""})
```
