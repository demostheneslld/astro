#####################################
########## ASTRO HEADER #############
#####################################

def scriptsummary(script, inputs, outputs):
	import os
	# SCRIPT SUMMARY
	print("\n\n\n######################################################\n")
	if '__file__' in globals():
	    print("CURRENT SCRIPT:\n" + str(os.path.realpath(__file__)) + "\n")
	print("INPUT FOLDERS:")
	for key in inputs:
	    print(inputs[key])
	print("\nOUTPUT FOLDERS:")
	for key in outputs:
	    print(outputs[key])
	print("\n######################################################\n")