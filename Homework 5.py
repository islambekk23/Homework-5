immutable_var = 5, 23, 'future', True
tuple_ = immutable_var
print(tuple_)
#tuple_[0] = 123
#print(tuple_[0])  # так как команда tuple является одним из команд неизменного типа, вот из-за этого нельзя изменить кортеж.

mutable_list = [7, 'brain', 'last']
print(mutable_list)