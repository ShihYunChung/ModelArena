import torch.nn as nn
from torchvision import models
from timm import create_model

def initialize_all_models(num_classes, pretrained=False):
    models_dict = {}

    # AlexNet
    models_dict["alexnet"] = models.alexnet(pretrained=pretrained, num_classes=num_classes)

    # VGG16
    vgg16 = models.vgg16(pretrained=pretrained)
    vgg16.classifier[6] = nn.Linear(vgg16.classifier[6].in_features, num_classes)
    models_dict["vgg16"] = vgg16

    # GoogleNet
    googlenet = models.googlenet(pretrained=pretrained, aux_logits=True, transform_input=False)
    googlenet.fc = nn.Linear(googlenet.fc.in_features, num_classes)
    googlenet.aux1.fc2 = nn.Linear(googlenet.aux1.fc2.in_features, num_classes)
    googlenet.aux2.fc2 = nn.Linear(googlenet.aux2.fc2.in_features, num_classes)
    models_dict["googlenet"] = googlenet

    # ResNet18
    resnet18 = models.resnet18(pretrained=pretrained, zero_init_residual=False)
    resnet18.fc = nn.Linear(resnet18.fc.in_features, num_classes)
    models_dict["resnet18"] = resnet18

    # SqueezeNet
    squeezenet = models.squeezenet1_0(pretrained=pretrained, num_classes=num_classes)
    squeezenet.classifier[1] = nn.Conv2d(512, num_classes, kernel_size=(1, 1), stride=(1, 1))
    models_dict["squeezenet"] = squeezenet

    # MobileNetV2
    mobilenet_v2 = models.mobilenet_v2(pretrained=pretrained, width_mult=1.0, round_nearest=8)
    mobilenet_v2.classifier[1] = nn.Linear(mobilenet_v2.classifier[1].in_features, num_classes)
    models_dict["mobilenet_v2"] = mobilenet_v2

    # EfficientNet-B0
    efficientnet_b0 = models.efficientnet_b0(pretrained=pretrained)
    efficientnet_b0.classifier[1] = nn.Linear(efficientnet_b0.classifier[1].in_features, num_classes)
    models_dict["efficientnet_b0"] = efficientnet_b0

    # Swin Transformer
    swin_t = models.swin_t(pretrained=pretrained, num_classes=num_classes)
    swin_t.head = nn.Linear(swin_t.head.in_features, num_classes)
    models_dict["swin_t"] = swin_t

    # Xception
    xception = create_model('xception', pretrained=pretrained, num_classes=num_classes, drop_rate=0.2)
    models_dict["xception"] = xception

    # ConvNeXt-Tiny
    convnext_tiny = create_model('convnext_tiny', pretrained=pretrained, num_classes=num_classes, drop_path_rate=0.1)
    models_dict["convnext_tiny"] = convnext_tiny

    # MNASNet
    mnasnet = models.mnasnet1_0(pretrained=pretrained)
    mnasnet.classifier[1] = nn.Linear(mnasnet.classifier[1].in_features, num_classes)
    models_dict["mnasnet"] = mnasnet

    return models_dict
