#include<ros.h>
#include<asv_msgs/MotorCmd.h>
#include<std_msgs/Int32.h>
#include<math.h>
#include<Servo.h>

byte servoPin_R = 2;
byte servoPin_L = 3;
byte servoPin_V = 4;

int rightSp = 1500;
int leftSp = 1500;
int verticalSp = 1500;

Servo servo_r;
Servo servo_l;
Servo servo_v;

ros::NodeHandle nh;
//std_msgs::Int32 pub_msg;

void cbMotor(const asv_msgs::MotorCmd& msg){
    rightSp = int(msg.right*400) + 1500;
    leftSp = int(msg.left*400) + 1500;
    verticalSp = int(msg.vertical*400) + 1500;
    //pub_msg.data = horizontalSp;
}

ros::Subscriber<asv_msgs::MotorCmd> sub("motor_cmd",cbMotor);
//ros::Publisher test("/test", &pub_msg);

void setup(){
    nh.initNode();
    nh.subscribe(sub);
    //nh.advertise(test);
    servo_r.attach(servoPin_R);
    servo_l.attach(servoPin_L);
    servo_v.attach(servoPin_V);
    servo_r.writeMicroseconds(1500);
    servo_l.writeMicroseconds(1500);
    servo_v.writeMicroseconds(1500);
    delay(7000);
}

void loop(){
    servo_r.writeMicroseconds(rightSp);
    servo_l.writeMicroseconds(leftSp);
    servo_v.writeMicroseconds(verticalSp);
    //test.publish( &pub_msg );
    nh.spinOnce();
    delay(100);
}
