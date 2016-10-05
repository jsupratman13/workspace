package workspace;
import java.awt.geom.*;
import java.util.*;
import robocode.*;

public class JSBot2 extends AdvancedRobot
{
	Tools tools;
	EnemyBot target;
	double selfEnergy;
	Point2D.Double destination;
	Point2D.Double selfPos;
	Map enemyList = new HashMap();
	int scanFlag = 0;
	boolean initial = true;

	public void onScannedRobot(ScannedRobotEvent e){
		EnemyBot enemy = (EnemyBot)enemyList.get(e.getName());
		if(enemy == null){
			System.out.println("detected new enemy: "+ enemy.name);
			enemy = new EnemyBot();
			enemyList.put(e.getName(), enemy);
		}
		enemy.name = e.getName();
		enemy.isAlive = true;
		enemy.energy = e.getEnergy();
		enemy.dist = e.getDistance();
		enemy.vel = e.getVelocity();
		enemy.bearing = e.getBearing();
		
		if((enemy.dist < target.dist && enemy.energy < target.energy) || initial){
			System.out.println("new target: "+ enemy.name);
			target = enemy;
			initial = false;
		}
	}

	public void onRobotDeath(RobotDeathEvent e){
		EnemyBot enemy = (EnemyBot)enemyList.get(e.getName());
		if(enemy != null){
			enemy.isAlive = false;
		}
	}
	
	public void onHitRobot(HitRobotEvent e){
		double absBearing = getHeading() + e.getBearing();
		double bearingFromGun = tools.normalRelativeAngle(absBearing - getGunHeading());
		
		turnGunRight(bearingFromGun);
		fire(5);
	}

	public void scanning(){
		if((scanFlag < 10) && (getOthers() == 1)){
		
		}
		else{
			turnRadarRight(9999);
		}
	}	

	public void shootTarget(){ 

	}

	public void move(Point2D targ){
		System.out.println(selfPos.getX() + " " + targ.getX());
		double distance = selfPos.distance(targ);
		double angle = tools.normalRelativeAngle(tools.absBearingAng(selfPos, targ) - getHeading());
		if (Math.abs(angle) > 90){
			distance *= -1.0;
			if(angle>0){
				angle -= 180;
			}else{
				angle += 180;
			}
		}
		System.out.println("moving: " + angle + " "+ distance);
		setTurnRight(angle);
		setAhead(distance);
	}

	public void run(){
		tools = new Tools();
		target = new EnemyBot();
		destination = new Point2D.Double(getX(), getY());
		selfPos = new Point2D.Double(getX(), getY());
		System.out.println(getX() + " " + getY());
		destination.setLocation(50, 50);
		System.out.println("start!");
		while(true){
			scanFlag++;
			selfEnergy = getEnergy();
			selfPos.setLocation(getX(), getY());	
			move(destination);
			scanning();
			execute();
		}
	}	
}
class EnemyBot{
	String name;
	boolean isAlive;
	double energy;
//	Point2D.Double pos;
	double dist;
	double vel;
	double bearing;
}

class Tools{	

	public double absBearingAng(Point2D src, Point2D targ){
		return Math.toDegrees(absBearingRad(src, targ));
	}

	public double absBearingRad(Point2D src, Point2D targ){
		return Math.atan2(targ.getX()-src.getX(), targ.getY()-src.getY()); 
	}
	
	public double normalRelativeAngle(double ang){
		double relAng = ang % 360;
		if(relAng <= -180){
			return 180 + (relAng % 180);
		}
		else if(relAng > 180){
			return -180 + (relAng % 180);
		}
		else{
			return relAng;
		}
	}
	
	public double normalRelativeRad(double rad){
		double ang = normalRelativeAngle(Math.toDegrees(rad));
		return Math.toRadians(ang);
	}

	public double distance(Point2D src, Point2D targ){ 
		return Math.sqrt(Math.pow((src.getX()-targ.getX()),2) + Math.pow((src.getY()-targ.getY()),2));
	}	
/*
	public double distance(double[] src, double[] targ){
		return Math.sqrt(Math.pow((src[0]-targ[0]),2) + Math.pow((src[1]-targ[1]),2));
	}
*/
}

