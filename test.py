from main import parse_option

if __name__ == '__main__':
    _, config = parse_option()
    if getattr(config.train, 'lr_noise_pct', None) is not None:
        print(getattr(config.train, 'lr_noise_pct'))
    else:
        print("Wrong")