class OptimisationConfig:
    def __init__(self, coverage_importance: float, reduction_importance: float, efficiency_importance: float,
                 min_coverage: float):
        self.coverage_importance = coverage_importance
        self.reduction_importance = reduction_importance
        self.efficiency_importance = efficiency_importance
        self.min_coverage = min_coverage
