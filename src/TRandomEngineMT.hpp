
// TRandomEngineMT2.hpp
// 
// Copyright 2016 Vincent Français <francais@clermont.in2p3.fr>
// 
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
// MA 02110-1301, USA.
// 
// 



#pragma once

#include "TRandomEngine.hpp"
#include "TGenMT.hpp"
//#include "MT/dc.h"
#include "dcmt/include/dc.h"

class TRandomEngineMT : public TRandomEngine {
	public:
		TRandomEngineMT() : TRandomEngine() {
			rand = TGenMT();
		}
		TRandomEngineMT(ulong init[], ulong length) : TRandomEngine() {
			rand = TGenMT(init, length);
		}
		TRandomEngineMT(std::string filename): TRandomEngine() {
			rand = TGenMT(filename);
		}
		
		TRandomEngineMT(ulong s): TRandomEngine() {
			rand = TGenMT(s);
		}
		
		double RandU01() { 
			return rand.mtRand(); 
		}
		
		std::string Generator() { 
			return "Mersenne-Twister"; 
		}
		
	private:
	TGenMT rand;
};



