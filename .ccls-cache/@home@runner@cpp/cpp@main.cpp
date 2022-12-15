#include <iostream>
 
int compare(int a, int b){
    if(a>b){
        std::cout<<a<<" is greater than "<<b<<"\n"<<std::endl;
    }
    else if(a==b){
        std::cout<<a<<" is equal to "<<b<<"\n"<<std::endl;
    }
    else{
        std::cout<<a<<" is less than "<<b<<"\n"<<std::endl;
    }
    return 0;
}
 
int factorial(int n){
    int placehold = 1;
    for(int i=1; i<n+1; i++){
        placehold = placehold*i;
    }
    std::cout<<"Factorial of "<<n<<" is: "<<placehold<<"\n"<<std::endl;
    return 0;
}
 
int main()
{
    std::cout<<"\nHello World\n"<<std::endl;
    int a = 1;
    int b = 3;
    int result = compare(a,b);
    int product = factorial(b);
    return 0;
}