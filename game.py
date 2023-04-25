from qiskit import QuantumCircuit, Aer
import numpy as np
import streamlit as st

def quantum_superposition():
  """
  The method helps to create a single qubit Quantum Superposition circuit
  """
  # initialize a quantum circuit
  circuit = QuantumCircuit(1,1)

  # apply hadamard gate
  circuit.h(0)

  # apply measurement
  circuit.measure(0,0)

  # get the simulator
  simulator = Aer.get_backend('aer_simulator')

  # get the results
  result = simulator.run(circuit).result().get_counts()

  return result

def get_random_value():
  """
  The method helps to get a random value from |0> or |1>
  """
  # get the result of single qubit superposition circuit
  res = quantum_superposition()

  # get the frequency of each outcome
  values = list(res.values())

  # get the two possible results as list
  keys = list(res.keys())

  # get the outcome with higher frequency 
  random_value = '|' + str(keys[np.argmax(values)]) + '>'
  return random_value



#####

def validate(arr):
  """
  The Method checks if the game is finished!
  Parameters:
  arr (numpy array) : The array that serves as the board
  Returns:
  returns 0 if any of the winning condition is satisfied by any of the player
  else returns 1
  """
  
  # define a boolean variable
  flag = True
  zero_ket = '|0>'
  one_ket = '|1>'

  # Checks for the principal diagonal condition w.r.t. user
  if arr[0,0]==one_ket and arr[1,1]==one_ket and arr[2,2]==one_ket:
    st.success('User has won!')
    flag = False

  # Checks for the principal diagonal condition w.r.t. computer
  elif arr[0,0]==zero_ket and arr[1,1]==zero_ket and arr[2,2]==zero_ket:
    st.success('Computer wins!')
    flag = False

  # Checks for the second diagonal condition w.r.t. user
  elif arr[0,2]==one_ket and arr[1,1]==one_ket and arr[2,0]==one_ket:
    st.success('User has won!')
    flag = False

  # Checks for the second diagonal condition w.r.t. computer
  elif arr[0,2]==zero_ket and arr[1,1]==zero_ket and arr[2,0]==zero_ket:
    st.success('Computer wins!')
    flag = False

  if not flag:
    return 0

  # we execute the below for loops iff any of the above conditions are not 
  # satisfied
  if flag:
    
    # Checks if any of the row conquered by user
    for index in [0,1,2]:
      if (list(arr[index])==[one_ket,one_ket,one_ket]):
        st.success('User has won!')
        return 0
        
    # Checks if any of the row conquered by computer
    for index in [0,1,2]:
      if (list(arr[index])==[zero_ket,zero_ket,zero_ket]):
        st.success("Computer wins!")
        return 0

    # Checks if any of the column conquered by user
    for index in [0,1,2]:
      if (list(arr[:,index])==[one_ket,one_ket,one_ket]):
        st.success('User has won!')
        return 0

    # Checks if any of the column conquered by computer
    for index in [0,1,2]:
      if (list(arr[:,index])==[zero_ket,zero_ket,zero_ket]):
        st.success('Computer wins!')
        return 0

    # Check if it's a draw
    if '|ψ>' not in arr:
      st.write("It's a draw!")
      return 0
  # if none of the conditions are satisfied, 1 is returned.
  return 1
