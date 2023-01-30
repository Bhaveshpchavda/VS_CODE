#include<iostream>
#include<string.h>
#define TEAM 2
using namespace std;


class PlayerDetails{
	public:
	int year,match,ing,avg,srate,wkt,eco,flag;

	void getData(){
	// comman
	
		cout<<"\n Enter Year :";
		cin>>year;
		cout<<"\n Enter No of matches played : ";
		cin>>match;
		cout<<"\n Enter no od innings played : ";
		cin>>ing;
	}
	void getBatsmanData(){
	// batsman
		getData();
		cout<<"\n Enter Playing average of a player : ";
		cin>>avg;
		cout<<"\n Enter Strike rate :";
		cin>>srate;
	}
	void getBowlerData(){
	// bowler
		getData();
		cout<<"\nEnter Wickets : ";
		cin>>wkt;
		cout<<"\nEnter Economy : ";
		cin>>eco;
	}

};

class Player{

	public:
	char name[20],type[20];
	PlayerDetails pd[3]; // 2018 2019 2020 2021
	void getData(){
		cout<<"\nEnter Player Name : ";
		cin>>name;
		cout<<"\nEnter Player Type (batsman / bowler) : ";
		cin>>type;
	}
	/*
	void displayBatsman(){
	cout<<year<<"\t"<<name<<"\t"<<match<<"\t"<<ing<<"\t"<<avg<<"\t"<<srate<<endl;
	} */
				

};
class Team{
	public:
	Player p[15]; // 15 times

};
int main(){
	int i,j,sum=0;
	

	Team sa; //

	for(i=0;i<TEAM;i++){
		sa.p[i].getData();
		// name type
		if(strcmp(sa.p[i].type,"batsman")==0){
			for(j=0;j<3;j++){ // 3 years 4
				sa.p[i].pd[j].getBatsmanData();
			}
			cout<<"\n---------------------------------\n";
		}
		else {
			for(j=0;j<3;j++){ // j<4
				sa.p[i].pd[j].getBowlerData();
			}
		}
	}

//printing part
	for(i=0;i<TEAM;i++){
		cout<<"\nPalyer Name : "<<sa.p[i].name;
		cout<<"\nPLayer Type : "<<sa.p[i].type;
		if(strcmp(sa.p[i].type,"batsman")==0){
		cout<<"\n\nYear\tMatch\tIning\tAverage\tStrikeRate\n";
		 for(j=0;j<3;j++){
			cout<<"\n"<<sa.p[i].pd[j].year<<"\t"<<sa.p[i].pd[j].match<<"\t"<<sa.p[i].pd[j].ing<<"\t"<<sa.p[i].pd[j].avg<<"\t"<<sa.p[i].pd[j].srate;
		

		}
	 }

		else if(strcmp(sa.p[i].type,"bowler")==0){
		cout<<"\n\nYear\tMatch\tIning\tWicket\tEconomy\n";
		 for(j=0;j<3;j++){

			cout<<"\n"<<sa.p[i].pd[j].year<<"\t"<<sa.p[i].pd[j].match<<"\t"<<sa.p[i].pd[j].ing<<"\t"<<sa.p[i].pd[j].wkt<<"\t"<<sa.p[i].pd[j].eco;
		 }
		}
		cout<<"\n--------****--------\n";
	}
//condition part

		 for ( i = 0; i < 3; i++)
                    {
                      if(strcmp(sa.p[i].type, "batsman") == 0){
					  for(j=0;j<3;j++){	 
			     
				 	  if(sa.p[i].pd[j].avg>=40){	   						
						   					    sa.p[i].pd[j].flag++;
											   } 
			 	      else{
						  
						   //flag=0;
					      }	
					 }				 											
				} // end of batsman
						 if(strcmp(sa.p[i].type, "bowler") == 0){
							for(j=0;j<3;j++){	 
				 	 			 if(sa.p[i].pd[j].wkt>=150){
						   						cout<<sa.p[i].name<<"player is selected"<<endl;
														   } 
			 	      			 else{
						   			cout<<sa.p[i].name<<"player is not selected"<<endl;
					      			 }	
					 			}// end of j bowler
						 }// end of bowler
					}
 for ( i = 0; i < 3; i++)
 {
 if(sa.p[i].pd[j].flag==3){
	cout<<sa.p[i].name<<"player is selected"<<endl;
 }	
 else{
 	cout<<sa.p[i].name<<"player is not selected"<<endl;
}
}
for(i=0;i<2;i++){ 
sum=0;
for(j=0;j<3;j++){
sum =sum+sa.p[i].pd[j].wkt;
}
cout<<"sum is "<<sum;
}
return 0;
} 