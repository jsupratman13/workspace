private void goTo(Point2D point){
	double distance = location.distance(point);
	double angl e = normalRelativeAngle(absoluteBearing(location, point) - getHeading());
	if (Math.abs(angle) > 90.0){
		distance *= -1.0;
		if (angle > 0.0){
			angle -= 180.0;
		}else{
			angle += 180.0;
		}
	}
	setTurnRight(angle);
	setAhead(distance);
}

private double absoluteBearing(Point2D source, Point2D target){
	return Math.toDegrees(Math.atan2(target.getX()-source.getX(), target.getY()-source.getY()));
}

private double normalRelativeAngle(double angle){
	double relativeAngle = angle % 360;
	if(relativeAngle <= -180)
		return 180 + (relativeAngle % 180);
	else if (relativeAngle > 180)
		return -180 + (relativeAngle % 180);
	else
		return relativeAngle;
}

private void translateInsideField(Point2D point, double margin){
	double X = Math.max(margin, Math.min(fieldRectangle.getWidth() - margin, point.getX()));
	double Y = Math.max(margin, Math.min(fieldRectangle.getHeight() - margin, point.getY()));
	point.setLocation(X,Y);
}


Point2D destination..
...
translateInsideField(dstination, 35);
goTo(destination);
