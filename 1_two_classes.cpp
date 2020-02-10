#include<iostream>
#include<vector>
#include<string>
#include<set>
using namespace std;

class Person{
  private:
	string name;
	float x, y;

  public:

  	string get_name(){
  		return this->name;
  	}
  	void set_name(string name){
  		this->name = name;
  	}

  	void move(float x, float y){
  		this->x += x;
  		this->y += y;
  	}

};

class Bus{

private:
	string number;
	float x, y;

	vector<Person*> persons;

public:

	void add_person(Person *p){
		this->persons.push_back(p);
	}

	void remove_person(Person *p){
		set<person>iterator it = this->persons.find(p)
		it.erase()
	}




};


int main(){

	cout<<"it's on"<<endl;

	return 0;
}





