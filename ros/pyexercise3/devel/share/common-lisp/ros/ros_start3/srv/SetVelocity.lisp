; Auto-generated. Do not edit!


(cl:in-package ros_start3-srv)


;//! \htmlinclude SetVelocity-request.msg.html

(cl:defclass <SetVelocity-request> (roslisp-msg-protocol:ros-message)
  ((linear_velocity
    :reader linear_velocity
    :initarg :linear_velocity
    :type cl:float
    :initform 0.0)
   (angular_velocity
    :reader angular_velocity
    :initarg :angular_velocity
    :type cl:float
    :initform 0.0))
)

(cl:defclass SetVelocity-request (<SetVelocity-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetVelocity-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetVelocity-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_start3-srv:<SetVelocity-request> is deprecated: use ros_start3-srv:SetVelocity-request instead.")))

(cl:ensure-generic-function 'linear_velocity-val :lambda-list '(m))
(cl:defmethod linear_velocity-val ((m <SetVelocity-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_start3-srv:linear_velocity-val is deprecated.  Use ros_start3-srv:linear_velocity instead.")
  (linear_velocity m))

(cl:ensure-generic-function 'angular_velocity-val :lambda-list '(m))
(cl:defmethod angular_velocity-val ((m <SetVelocity-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_start3-srv:angular_velocity-val is deprecated.  Use ros_start3-srv:angular_velocity instead.")
  (angular_velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetVelocity-request>) ostream)
  "Serializes a message object of type '<SetVelocity-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'linear_velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angular_velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetVelocity-request>) istream)
  "Deserializes a message object of type '<SetVelocity-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'linear_velocity) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angular_velocity) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetVelocity-request>)))
  "Returns string type for a service object of type '<SetVelocity-request>"
  "ros_start3/SetVelocityRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetVelocity-request)))
  "Returns string type for a service object of type 'SetVelocity-request"
  "ros_start3/SetVelocityRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetVelocity-request>)))
  "Returns md5sum for a message object of type '<SetVelocity-request>"
  "f6aaad2e58fe90e46753c2e927c41798")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetVelocity-request)))
  "Returns md5sum for a message object of type 'SetVelocity-request"
  "f6aaad2e58fe90e46753c2e927c41798")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetVelocity-request>)))
  "Returns full string definition for message of type '<SetVelocity-request>"
  (cl:format cl:nil "~%float64 linear_velocity~%float64 angular_velocity~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetVelocity-request)))
  "Returns full string definition for message of type 'SetVelocity-request"
  (cl:format cl:nil "~%float64 linear_velocity~%float64 angular_velocity~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetVelocity-request>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetVelocity-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetVelocity-request
    (cl:cons ':linear_velocity (linear_velocity msg))
    (cl:cons ':angular_velocity (angular_velocity msg))
))
;//! \htmlinclude SetVelocity-response.msg.html

(cl:defclass <SetVelocity-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SetVelocity-response (<SetVelocity-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetVelocity-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetVelocity-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_start3-srv:<SetVelocity-response> is deprecated: use ros_start3-srv:SetVelocity-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetVelocity-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_start3-srv:success-val is deprecated.  Use ros_start3-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetVelocity-response>) ostream)
  "Serializes a message object of type '<SetVelocity-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetVelocity-response>) istream)
  "Deserializes a message object of type '<SetVelocity-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetVelocity-response>)))
  "Returns string type for a service object of type '<SetVelocity-response>"
  "ros_start3/SetVelocityResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetVelocity-response)))
  "Returns string type for a service object of type 'SetVelocity-response"
  "ros_start3/SetVelocityResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetVelocity-response>)))
  "Returns md5sum for a message object of type '<SetVelocity-response>"
  "f6aaad2e58fe90e46753c2e927c41798")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetVelocity-response)))
  "Returns md5sum for a message object of type 'SetVelocity-response"
  "f6aaad2e58fe90e46753c2e927c41798")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetVelocity-response>)))
  "Returns full string definition for message of type '<SetVelocity-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetVelocity-response)))
  "Returns full string definition for message of type 'SetVelocity-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetVelocity-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetVelocity-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetVelocity-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetVelocity)))
  'SetVelocity-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetVelocity)))
  'SetVelocity-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetVelocity)))
  "Returns string type for a service object of type '<SetVelocity>"
  "ros_start3/SetVelocity")