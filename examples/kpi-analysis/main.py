from dataclasses import dataclass, field
from faker import Faker
import random
from typing import List

fake = Faker()


@dataclass
class DeltaPartition:
    """A single partition of a delta with its value and description."""
    value: float
    description: str


@dataclass
class Delta:
    """Represents a delta between two metrics with its partitions."""
    name: str
    total_value: float
    partitions: List[DeltaPartition] = field(default_factory=list)


@dataclass
class KPIMetrics:
    """Contains Plan, Forecast, and Fact values for a KPI."""
    plan: float
    forecast: float
    fact: float


@dataclass
class KPI:
    """Complete KPI with metrics and all deltas."""
    name: str
    metrics: KPIMetrics
    deltas: List[Delta] = field(default_factory=list)


def generate_random_value(min_val: float = 10.0, max_val: float = 150.0) -> float:
    """Generate a random float with 2 decimal places."""
    return round(random.uniform(min_val, max_val), 2)


def generate_description() -> str:
    """Generate a short business-like description for a delta partition."""
    templates = [
        f"Market {fake.word()} adjustment",
        f"{fake.company_suffix()} restructuring",
        f"Volume {random.choice(['increase', 'decrease', 'shift'])}",
        f"Price {random.choice(['optimization', 'correction', 'adjustment'])}",
        f"{fake.word().capitalize()} cost variance",
        f"FX {random.choice(['impact', 'effect', 'adjustment'])}",
        f"Seasonal {random.choice(['effect', 'trend', 'pattern'])}",
        f"Customer {random.choice(['mix change', 'churn', 'acquisition'])}",
        f"Supply chain {random.choice(['delay', 'optimization', 'cost'])}",
        f"Material cost {random.choice(['increase', 'savings', 'variance'])}",
        f"Labor {random.choice(['efficiency', 'cost change', 'reallocation'])}",
        f"Inventory {random.choice(['write-off', 'adjustment', 'revaluation'])}",
    ]
    return random.choice(templates)


def generate_partitions(total_delta: float, min_partitions: int = 1, max_partitions: int = 5) -> List[DeltaPartition]:
    """Generate partitions that sum up to the total delta."""
    if abs(total_delta) < 0.01:
        return [DeltaPartition(value=0.0, description="No variance")]

    num_partitions = random.randint(min_partitions, max_partitions)
    sign = 1 if total_delta >= 0 else -1
    abs_total = abs(total_delta)

    # Generate random proportions
    proportions = [random.random() for _ in range(num_partitions)]
    total_proportion = sum(proportions)

    # Calculate partition values
    partition_values = [round((p / total_proportion) * abs_total, 2)
                        for p in proportions]

    # Adjust last partition to ensure exact sum
    current_sum = sum(partition_values[:-1])
    partition_values[-1] = round(abs_total - current_sum, 2)

    # Apply sign and create partitions
    partitions = [
        DeltaPartition(
            value=round(val * sign, 2),
            description=generate_description()
        )
        for val in partition_values
    ]

    return partitions


def generate_deltas(metrics: KPIMetrics) -> List[Delta]:
    """Generate all three deltas with their partitions."""
    deltas_config = [
        ("Plan vs Forecast", metrics.plan - metrics.forecast),
        ("Plan vs Fact", metrics.plan - metrics.fact),
        ("Forecast vs Fact", metrics.forecast - metrics.fact),
    ]

    deltas = []
    for name, total_value in deltas_config:
        total_value = round(total_value, 2)
        partitions = generate_partitions(total_value)
        deltas.append(
            Delta(name=name, total_value=total_value, partitions=partitions))

    return deltas


def generate_kpi(name: str) -> KPI:
    """Generate a complete KPI with metrics and deltas."""
    metrics = KPIMetrics(
        plan=generate_random_value(),
        forecast=generate_random_value(),
        fact=generate_random_value()
    )
    deltas = generate_deltas(metrics)
    return KPI(name=name, metrics=metrics, deltas=deltas)


def generate_test_data(kpi_names: List[str] = None) -> List[KPI]:
    """Generate complete test data for all KPIs."""
    if kpi_names is None:
        kpi_names = ["Q3", "Q3 SB", "Cupra"]

    return [generate_kpi(name) for name in kpi_names]


def _print_kpi_header(kpi: KPI) -> None:
    """Print the KPI banner with Plan, Forecast, and Fact values."""
    print(f"\n{'='*60}")
    print(f"KPI: {kpi.name}")
    print(f"{'='*60}")
    print(f"  Plan:     {kpi.metrics.plan:>8.2f}")
    print(f"  Forecast: {kpi.metrics.forecast:>8.2f}")
    print(f"  Fact:     {kpi.metrics.fact:>8.2f}")


def _print_delta_header(delta: Delta) -> None:
    """Print a delta's name and total value."""
    print(f"\n  {delta.name}: {delta.total_value:+.2f}")


def print_test_data_top_n(kpis: List[KPI], top_n: int) -> None:
    """Pretty print the generated test data, showing only the top N partitions by abs(value) per delta."""
    for kpi in kpis:
        _print_kpi_header(kpi)

        for delta in kpi.deltas:
            _print_delta_header(delta)
            sorted_partitions = sorted(
                delta.partitions, key=lambda p: abs(p.value), reverse=True
            )
            top_partitions = sorted_partitions[:top_n]
            remaining_partitions = sorted_partitions[top_n:]
            actual_top = len(top_partitions)
            print(
                f"  Top {actual_top} Partition{'s' if actual_top != 1 else ''}:")
            for i, partition in enumerate(top_partitions, 1):
                print(
                    f"    {i}. {partition.value:+7.2f} : {partition.description}")
            if remaining_partitions:
                misc_sum = round(sum(p.value for p in remaining_partitions), 2)
                print(f"    {actual_top + 1}. {misc_sum:+7.2f} : Misc.")
            partition_sum = sum(p.value for p in top_partitions)
            print(f"    {'─'*40}")
            print(
                f"    Sum (top {actual_top}): {partition_sum:+7.2f} (Total: {delta.total_value:+.2f})")


def print_test_data(kpis: List[KPI]) -> None:
    """Pretty print the generated test data."""
    for kpi in kpis:
        _print_kpi_header(kpi)

        for delta in kpi.deltas:
            _print_delta_header(delta)
            print(f"  Partitions:")
            for i, partition in enumerate(delta.partitions, 1):
                print(
                    f"    {i}. {partition.value:+7.2f} : {partition.description}")
            partition_sum = sum(p.value for p in delta.partitions)
            print(f"    {'─'*40}")
            print(
                f"    Sum: {partition_sum:+7.2f} (Total: {delta.total_value:+.2f})")


# Example usage
if __name__ == "__main__":
    random.seed(1)  # For reproducibility

    test_data = generate_test_data()
    print_test_data_top_n(test_data, 2)
    # print_test_data(test_data)

    # # You can also access data programmatically
    # print("\n\nProgrammatic access example:")
    # kpi = test_data[0]
    # print(f"First KPI name: {kpi.name}")
    # print(f"Plan value: {kpi.metrics.plan}")
    # print(
    #     f"First delta partitions: {[(p.value, p.description) for p in kpi.deltas[0].partitions]}")
