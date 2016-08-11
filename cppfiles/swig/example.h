#pragma once
#include <string>
class ExampleClass{
	std::string m_msg;
	
	public:
		ExampleClass() : m_msg("Hello World!") {}
		const std::string& get_msg(){ return m_msg;}
		void set_msg(const std::string &msg){m_msg = msg;}
};
