#!/usr/bin/env python
# ==================================================================== #
# Copyright (C) 2022 - Automation Lab - Sungkyunkwan University
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
# ==================================================================== #

import glob
import os
import sys
import time

try:
	sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
		sys.version_info.major,
		sys.version_info.minor,
		'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
	pass

import carla

import argparse
import math


def update_weather(index: int):
	if index == -1:
		return 0, carla.WeatherParameters.ClearNoon, "ClearNoon"
	if index == 0:
		return 1, carla.WeatherParameters.CloudyNoon, "CloudyNoon"
	if index == 1:
		return 2, carla.WeatherParameters.WetNoon, "WetNoon"
	if index == 2:
		return 3, carla.WeatherParameters.WetCloudyNoon, "WetCloudyNoon"
	if index == 3:
		return 4, carla.WeatherParameters.MidRainyNoon, "MidRainyNoon"
	if index == 4:
		return 5, carla.WeatherParameters.HardRainNoon, "HardRainNoon"
	if index == 5:
		return 6, carla.WeatherParameters.SoftRainNoon, "SoftRainNoon"
	if index == 6:
		return 7, carla.WeatherParameters.ClearSunset, "ClearSunset"
	if index == 7:
		return 8, carla.WeatherParameters.CloudySunset, "CloudySunset"
	if index == 8:
		return 9, carla.WeatherParameters.WetSunset, "WetSunset"
	if index == 9:
		return 10, carla.WeatherParameters.WetCloudySunset, "WetCloudySunset"
	if index == 10:
		return 11, carla.WeatherParameters.MidRainSunset, "MidRainSunset"
	if index == 11:
		return 12, carla.WeatherParameters.HardRainSunset, "HardRainSunset"
	if index == 12:
		return 13, carla.WeatherParameters.SoftRainSunset, "SoftRainSunset"
	return -1, None, None



def main():
	argparser = argparse.ArgumentParser(
		description=__doc__)
	argparser.add_argument(
		'--host',
		metavar='H',
		default='127.0.0.1',
		help='IP of the host server (default: 127.0.0.1)')
	argparser.add_argument(
		'-p', '--port',
		metavar='P',
		default=2000,
		type=int,
		help='TCP port to listen to (default: 2000)')
	argparser.add_argument(
		'-ni', '--number_image',
		metavar='FACTOR',
		default=5,
		type=int,
		help='Number of position will load images')
	args = argparser.parse_args()

	client = carla.Client(args.host, args.port)
	client.set_timeout(5.0)
	world = client.get_world()


	# for num in range(args.number_image):	
	num = -1
	while True:
		num += 1
		index = -1
		while True:
			index, weather, weather_name = update_weather(index)
			

			if index == -1:
				break

			world.set_weather(weather)
			print(f"Number of image : {num} - index : {index} - weather : {weather_name}")
			time.sleep(3)
			



if __name__ == '__main__':

	main()
