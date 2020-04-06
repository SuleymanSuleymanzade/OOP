#include<iostream>
#include<vector>
#include<string>
#include<set>

using namespace std;


class Bus{
  private:
	string number;
	pair<float, float> coordinates;
	set<class Person*> passengers;

  public:
    Bus(string number="Default", pair<float, float> coordinates = {0.,0.}){
        this->number = number;
        this->coordinates = coordinates;
    }

	void add_passenger(Person *p){
		this->passengers.insert(p);
	}
    
	void remove_passenger(string name);    
    void show_passengers();
    void move(float x, float y); 
};

class Person{
  private:
	string name;
	pair<float, float> coordinates;
    Bus* bus;
  public:
    
    Person(string name = "unknown", pair<float, float> coordinates = {0., 0.}){
        this->name = name;
        this->coordinates = coordinates;
        this->bus = NULL;
    }
    
    bool operator<(Person *per){ // for set<Person* >::find method
        return name < per->name;
    }

  	string get_name(){
  		return this->name;
  	}
  	void set_name(string name){
  		this->name = name;
  	}

    void get_into_the_bus(Bus *b){
        this->bus = b;
        b->add_passenger(this);
    }
    void get_out_of_bus(){
        if(this->bus != NULL){
            this->bus->remove_passenger(this->name);
        }
    }

    void move(float x, float y){
        this->coordinates.first += x;
        this->coordinates.second += y;
    }
};

void Bus::show_passengers(){
    for(auto passenger: passengers){
        cout<<passenger->get_name()<<endl;
    } 
}
 
void Bus::remove_passenger(string name){
    
	for(auto it = this->passengers.begin(); it != this->passengers.end(); it++){
           if((*it)->get_name() == name)
               it = passengers.erase(it);
       }
}

void Bus::move(float x, float y){
    this->coordinates.first += x;
    this->coordinates.second += y;
    
    for(auto passenger: passengers){
        passenger->move(x, y);
    }
}

int main(){

	Person* p1 = new Person("Andy");
    Person* p2 = new Person("Matt");
    Person* p3 = new Person("Steve");

    Bus* bus = new Bus("123-A-X");

    p1->get_into_the_bus(bus);
    p2->get_into_the_bus(bus);
    p3->get_into_the_bus(bus);

    bus->show_passengers();
    cout<<"--------------------------"<<endl;
    bus->move(2., 7.);
    
    p1->get_out_of_bus();
    
    bus->show_passengers();
    
    cout<<"------------------------"<<endl;

    p2->get_out_of_bus();
    bus->move(3., 3.);
    bus->show_passengers();

	return 0;
}





