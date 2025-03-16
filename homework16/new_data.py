def hidden_function(x, y):
    #function with Gaussian noise added
    noise = np.random.normal(0, 0.2, x.shape)
    return np.sin(x) + np.cos(y) + noise

#data
x_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
y_data = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
X, Y = np.meshgrid(x_data, y_data)

#apply
pattern = hidden_function(X, Y)
N, D_in, H, D_out = 1000, 2, 50, 1

#input data
x = torch.randn(N, D_in) * 3.1415
y = (x[:, 0].sin() + x[:, 1].cos()).unsqueeze(1)

#apply noise
noise = torch.randn(N, D_out) * 0.2  # More noise than before
y += noise

#numpy for visualization
x_values = x.numpy()[:, 0]
y_values = x.numpy()[:, 1]
color_values = y.numpy().flatten()