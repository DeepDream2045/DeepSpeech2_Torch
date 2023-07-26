
import torch

from deepspeech2 import DeepSpeech2

batch_size = 3
sequence_length = 14321
dimension = 80

cuda = torch.cuda.is_available()
device = torch.device('cuda' if cuda else 'cpu')

inputs = torch.rand(batch_size, sequence_length, dimension).to(device)  # BxTxD
input_lengths = torch.LongTensor([14321, 14300, 13000]).to(device)

print("Deep Speech 2 Model Test..")
model = DeepSpeech2(num_classes=10, input_dim=dimension).to(device)
output = model.recognize(inputs, input_lengths)

print(output)
print(output.size())
