from fastbook import *
from fastai.vision.widgets import *
class DataLoaders(GetAttr):
    def __init__(self, *loaders): self.loaders = loaders
    def __getitem__(self, i): return self.loaders[i]
    train,valid = add_props(lambda i,self: self[i])

def Trainer(DataPath,Epochs=5,ShowTopLosses=True,NTopLosses=10):
    TrainingData = DataBlock(
        blocks=(ImageBlock, CategoryBlock), 
        get_items=get_image_files, 
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=Resize(128))

    TrainingData = TrainingData.new(
        item_tfms=RandomResizedCrop(224, min_scale=0.5),
        batch_tfms=aug_transforms())
    dls = TrainingData.dataloaders(DataPath)
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    learn.fine_tune(Epochs)
    if ShowTopLosses==True:
        interp = ClassificationInterpretation.from_learner(learn)
        interp.plot_confusion_matrix()
        interp.plot_top_losses(NTopLosses, nrows=NTopLosses)
    learn.export()
